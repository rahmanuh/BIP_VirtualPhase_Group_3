within gantry_system;

model exp_2_calib_damp_p
  type Length = Real(unit="m");
  type AngularDisp = Real(unit="rad");
  type AngularVelo = Real(unit="rad/s");
  type Mass = Real(unit="kg", min=0);
  type Damping = Real;
  type Acceleration = Real(unit="m/s2");
  type ControlSignal = Integer;

  parameter Mass m=0.2 "Mass of pendulum bob/container"; // 200 g
  parameter Length r=0.1 "Length of the rope connecting the pendulum bob to the trolley"; // 100 cm
  parameter Damping d_p=0.05 "Damping factor swinging of pendulum";
  parameter Acceleration g=9.8 "Constant for gravitational acceleration on the surface of the Earth (not Newton's gravitational constant!!)";
  
  // Variables
  AngularDisp theta "Angular displacement of the pendulum, w.r.t the trolley";
  AngularVelo omega "Angular velocity of the pendulum";
  
initial equation
  theta = 0.5235988; // 30 deg
  
equation
  der(theta) = omega;
  der(omega) = -( (d_p*omega) + (m*g*r*sin(theta)) ) / ( m*r^2 );

end exp_2_calib_damp_p;