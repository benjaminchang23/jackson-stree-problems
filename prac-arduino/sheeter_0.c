#include <Stepper.h>

enum sheeter_state {
    ESTOP,
    STANDBY,
    CALIBRATION,
    SHEET_LEFT,
    SHEET_LEFT_STOP,
    SHEET_RIGHT,
    SHEET_RIGHT_STOP,
    LOWER,

    _NUM_STATES
};

sheeter_state = STANDBY
const int stepsPerRevolutionHeight = 255;
const int stepsPerRevolutionTable = 255;
unsigned long debounceDelay = 50;

// info taken from: https://docs.arduino.cc/built-in-examples/digital/Debounce/
class Button {
public:
    Button(int button_pin)
    {
        last_debounce_time_ = 0;
        debounce_delay_ = debounceDelay; // ms
        button_pin_ = button_pin;
        button_state_ = 0;
        last_button_state_ = 0;
    };
    void Read();
private:
    // millisecond debounce timer
    unsigned long last_debounce_time_;
    unsigned long debounce_delay_;
    int button_pin_;
    int button_state_;
    int last_button_state_;
};

void Button::Read()
{
    int reading = digitalRead(button_pin_);

    if (reading != last_button_state_) {
        // reset the debouncing timer
        last_debounce_time_ = millis();
    }

    if ((millis() - last_debounce_time_) > debounce_delay_) {
        if (reading != button_state_) {
          button_state_ = reading;
        }
    }

    last_button_state_ = reading;
}

class StepperMotor {
public:
    StepperMotor(int, steps, int pin_0, int pin_1, int pin_2, int pin_3) {
        stepper_ = Stepper(steps, pin_0, pin_1, pin_2, pin3)
    };
    void Run();
    void SetSpeed(int motor_speed);
private:
    Stepper stepper_;
};

void StepperMotor::Run() {
    
}

void StepperMotor::SetSpeed(int motor_speed) {
    stepper_.setSpeed(motor_speed);
}

void setup() {
  // initialize the serial port:
  Serial.begin(9600);
  StepperMotor leftHeightStepper(stepsPerRevolutionHeight, 8, 9, 10, 11);
  StepperMotor rightHeightStepper(stepsPerRevolutionHeight, 8, 9, 10, 11);
  StepperMotor tableStepper(stepsPerRevolutionTable, 8, 9, 10, 11);
  leftHeightStepper.SetSpeed()
}

void loop() {
  table.run()
  if (motorSpeed > 0) {
    myStepper
    // step 1/100 of a revolution:
    myStepper.step(stepsPerRevolution / 100);
  }
}