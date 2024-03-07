enum class sheeter_state_t {
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

// info taken from: https://docs.arduino.cc/built-in-examples/digital/Debounce/
class Button {
public:
    Button(int button_pin)
    {
        last_debounce_time_ = 0;
        debounce_delay_ = 50; // ms
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
    int reading = digitalRead(buttonPin);

    if (reading != last_button_state_)
    {
        // reset the debouncing timer
        last_debounce_time_ = millis();
    }

    if ((millis() - last_debounce_time_) > debounce_delay_)
    {
        if (reading != button_state_)
        {
          button_state_ = reading;
        }
    }

    last_button_state_ = reading;
}

class StepperMotor {
public:
    
private:
    int steps_;
};

class Sheeter {
public:
    void Run();
    void RunCalibration();

private:
    StepperMotor height_motor_left_;
    StepperMotor height_motor_right_;
    StepperMotor table_drive_motor_;
    Button height_motor_left_button_;
    Button height_motor_right_button_;
    Button start_button_;
    sheeter_state_t sheeter_state_;
};

void Sheeter::Run()
{
    switch (sheeter_state_)
    {
    case sheeter_state_t::ESTOP:
        height_motor_left_.Stop();
        height_motor_right_.Stop();
        table_drive_motor_.Stop();
        break;
    case sheeter_state_t::STANDBY:
        if (start_button_ == HIGH)
            sheeter_state_ = sheeter_state_t::SHEET_LEFT;
        break;
    case sheeter_state_t::CALIBRATION:
        /* code */
        break;
    case sheeter_state_t::SHEET_LEFT:
        /* code */
        break;
    case sheeter_state_t::SHEET_LEFT_STOP:
        /* code */
        break;
    case sheeter_state_t::SHEET_RIGHT:
        /* code */
        break;
    case sheeter_state_t::SHEET_RIGHT_STOP:
        /* code */
        break;
    case sheeter_state_t::LOWER:
        /* code */
        break;
    default:
      break;
    }
}

void Sheeter::RunCalibration()
{
    
}
 
void setup()
{
    Serial.begin(9600);
    ButtonRoller<7,8> board('X', 1.0, 2, 3);
    ButtonRoller<9,10> vertL('L', 1.0, 4, 5);
    ButtonRoller<11,12> vertR('L', 1.0, 6, 7);
    // new type tied to board for the top motor?
    board.calibrate();
    vertL.calibrate();
    vertR.calibrate();  
}

void loop()
{
    board.run();
    vertL.run();
    vertR.run();
}