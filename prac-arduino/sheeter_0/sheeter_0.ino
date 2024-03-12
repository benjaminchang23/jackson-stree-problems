#include <AccelStepper.h>
#include <MultiStepper.h>

// stepper pins
#define NORTH_STEPPER_STEP_PIN 0
#define NORTH_STEPPER_DIR_PIN 0

#define SOUTH_STEPPER_STEP_PIN 13
#define SOUTH_STEPPER_DIR_PIN 12

#define TABLE_STEPPER_STEP_PIN 0
#define TABLE_STEPPER_DIR_PIN 0

#define ROLLER_STEPPER_STEP_PIN 0
#define ROLLER_STEPPER_DIR_PIN 0

// control button pins
#define CONTROL_EAST_BUTTON_PIN 0
#define CONTROL_WEST_BUTTON_PIN 0
#define CONTROL_UP_BUTTON_PIN 0
#define CONTROL_DOWN_BUTTON_PIN 0
#define CONTROL_CALIBRATION_BUTTON_PIN 0

// signal button pins
#define LIMIT_EAST_PIN 0
#define LIMIT_WEST_PIN 0
#define LIMIT_NORTH_TOP_PIN 0
#define LIMIT_NORTH_BOT_PIN 0
#define LIMIT_SOUTH_TOP_PIN 0
#define LIMIT_SOUTH_BOT_PIN 0

// roller to table ratio
#define ROLLER_TO_TABLE_RATIO 2

enum class sheeter_state_t : uint8_t {
    ESTOP,
    STANDBY,
    CALIBRATION_EAST_WEST,
    CALIBRATION_NORTH_SOUTH,
    SHEET_EAST,
    SHEET_WEST,
    RAISE,
    LOWER,

    _NUM_STATES
};

enum class sheeter_direction_t : uint8_t {
    EAST,
    WEST,
    UP,
    DOWN
};

// MultiStepper TableControl;
// MultiStepper HeightControl;

bool north_cw_found = false;
bool north_ccw_found = false;
bool south_cw_found = false;
bool south_ccw_found = false;
bool table_cw_found = false;
bool table_ccw_found = false;

long north_height_positions[2]; // array for calibration
long south_height_positions[2]; // array for calibration
long table_positions[2]; // array for table positions

// info taken from: https://docs.arduino.cc/built-in-examples/digital/Debounce/
class Button {
public:
    Button(int button_pin)
    {
        button_pin_ = button_pin;
        pinMode(button_pin_, INPUT_PULLUP);
        button_state = LOW;
    };
    bool Pressed();
    void Read();
    int button_state;
private:
    int button_pin_;
};

bool Button::Pressed() {
    return button_state == HIGH;
}

void Button::Read() {
    button_state = digitalRead(button_pin_);
}

sheeter_state_t sheeter_state = sheeter_state_t::STANDBY;

Button ControlEast(CONTROL_EAST_BUTTON_PIN);
Button ControlWest(CONTROL_WEST_BUTTON_PIN);
Button ControlUp(CONTROL_UP_BUTTON_PIN);
Button ControlDown(CONTROL_DOWN_BUTTON_PIN);
Button ControlCalibration(CONTROL_CALIBRATION_BUTTON_PIN);
Button LimitEast(LIMIT_EAST_PIN);
Button LimitWest(LIMIT_WEST_PIN);
Button LimitNorthTop(LIMIT_NORTH_TOP_PIN);
Button LimitNorthBot(LIMIT_NORTH_BOT_PIN);
Button LimitSouthTop(LIMIT_SOUTH_TOP_PIN);
Button LimitSouthBot(LIMIT_SOUTH_BOT_PIN);

AccelStepper NorthStepper(AccelStepper::DRIVER, NORTH_STEPPER_STEP_PIN, NORTH_STEPPER_DIR_PIN);
AccelStepper SouthStepper(AccelStepper::DRIVER, SOUTH_STEPPER_STEP_PIN, SOUTH_STEPPER_DIR_PIN);
AccelStepper TableStepper(AccelStepper::DRIVER, TABLE_STEPPER_STEP_PIN, TABLE_STEPPER_DIR_PIN);
AccelStepper RollerStepper(AccelStepper::DRIVER, ROLLER_STEPPER_STEP_PIN, ROLLER_STEPPER_DIR_PIN);

// positive values are cw
void HeightCalibrationRoutine() {
    if (!north_cw_found) {
        NorthStepper.moveTo(100);
    }
    else if (!north_ccw_found) {
        NorthStepper.moveTo(-100);
    }
    else {
        NorthStepper.stop();
    }
    if (!south_cw_found) {
        SouthStepper.moveTo(100);
    }
    else if (!south_ccw_found) {
        SouthStepper.moveTo(-100);
    }
    else {
        SouthStepper.stop();
    }

    if (LimitNorthTop.Pressed()) {
        north_height_positions[?] = NorthStepper.currentPosition();
        NorthStepper.stop();
    }
    if (LimitNorthBot.Pressed()) {
        north_height_positions[?] = NorthStepper.currentPosition();
        NorthStepper.stop();
    }
    if (LimitSouthTop.Pressed()) {
        south_height_positions[?] = SouthStepper.currentPosition();
        SouthStepper.stop();
    }
    if (LimitSouthBot.Pressed()) {
        south_height_positions[?] = SouthStepper.currentPosition();
        SouthStepper.stop();
    }
    if (north_cw_found && north_ccw_found && south_cw_found && south_ccw_found) {
        sheeter_state = sheeter_state_t::CALIBRATION_EAST_WEST;
    }
}

// positive values are cw
void TableCalibrationRoutine() {
    if (!table_cw_found) {
        TableStepper.moveTo(100);
        RollerStepper.moveTo(100);
    }
    else if (!table_ccw_found) {
        TableStepper.moveTo(-100);
        RollerStepper.moveTo(-100);
    }
    else {
        TableStepper.stop();
    }

    if (LimitEast.Pressed()) {
        table_positions[?] = TableStepper.currentPosition();
        TableStepper.stop();
        RollerStepper.stop();
    }
    if (LimitWest.Pressed()) {
        table_positions[?] = TableStepper.currentPosition();
        TableStepper.stop();
        RollerStepper.stop();
    }
    if (table_cw_found && table_ccw_found) {
        sheeter_state = sheeter_state_t::STANDBY;
    }
}

void MoveTable(sheeter_direction_t move_dir) {
    int dir_multi = 1;
    if (move_dir == sheeter_direction_t::EAST) {
        dir_multi = -1;
    }
    TableStepper.moveTo(ROLLER_TO_TABLE_RATIO*dir_multi*100);
    RollerStepper.moveTo(dir_multi*100);
}

void MoveRoller(sheeter_direction_t move_dir) {
    int dir_multi = 1;
    if (move_dir == sheeter_direction_t::DOWN) {
        dir_multi = -1;
    }
    NorthStepper.moveTo(dir_multi*100);
    SouthStepper.moveTo(dir_multi*100);
}

void ReadButtons() {
    ControlEast.Read();
    ControlWest.Read();
    ControlUp.Read();
    ControlDown.Read();

    LimitEast.Read();
    LimitWest.Read();
    LimitNorthTop.Read();
    LimitNorthBot.Read();
    LimitSouthTop.Read();
    LimitSouthBot.Read();
}

void RunStateMachine() {
    switch (sheeter_state) {
    case sheeter_state_t::ESTOP:
        Serial.println("Error");
        NorthStepper.stop();
        SouthStepper.stop();
        TableStepper.stop();
        RollerStepper.stop();
        break;
    case sheeter_state_t::STANDBY:
        Serial.println("Standby");
        break;
    case sheeter_state_t::CALIBRATION_EAST_WEST:
        Serial.println("Cal EW");
        TableCalibrationRoutine();
        RunSteppers();
        break;
    case sheeter_state_t::CALIBRATION_NORTH_SOUTH:
        Serial.println("Cal NS");
        HeightCalibrationRoutine();
        RunSteppers();
        break;
    case sheeter_state_t::SHEET_EAST:
        Serial.println("East");
        MoveTable(sheeter_direction_t::EAST);
        RunSteppers();
        break;
    case sheeter_state_t::SHEET_WEST:
        Serial.println("West");
        MoveTable(sheeter_direction_t::WEST);
        RunSteppers();
        break;
    case sheeter_state_t::RAISE:
        Serial.println("Raise");
        MoveRoller(sheeter_direction_t::UP);
        RunSteppers();
        break;
    case sheeter_state_t::LOWER:
        Serial.println("Lower");
        MoveRoller(sheeter_direction_t::DOWN);
        RunSteppers();
        break;
    default:
        break;
    }
}

void RunSteppers() {
    NorthStepper.run();
    SouthStepper.run();
    TableStepper.run();
    RollerStepper.run();
    // if (!NorthStepper.run() && NorthStepper.distanceToGo() != 0) {
    //     sheeter_state = sheeter_state_t::ESTOP;
    // }
    // if (!SouthStepper.run() && SouthStepper.distanceToGo() != 0) {
    //     sheeter_state = sheeter_state_t::ESTOP;
    // }
    // if (!TableStepper.run() && TableStepper.distanceToGo() != 0) {
    //     sheeter_state = sheeter_state_t::ESTOP;
    // }
    // if (!RollerStepper.run() && RollerStepper.distanceToGo() != 0) {
    //     sheeter_state = sheeter_state_t::ESTOP;
    // }
}

void setup() {
    // initialize the serial port:
    Serial.begin(9600);

    NorthStepper.setMaxSpeed(200.0);
    SouthStepper.setMaxSpeed(200.0);
    TableStepper.setMaxSpeed(200.0);
    RollerStepper.setMaxSpeed(200.0);

    SouthStepper.setAcceleration(100.0);
    NorthStepper.setAcceleration(100.0);
    TableStepper.setAcceleration(100.0);
    RollerStepper.setAcceleration(100.0);
}

void loop() {
    ReadButtons();
    RunStateMachine();
}