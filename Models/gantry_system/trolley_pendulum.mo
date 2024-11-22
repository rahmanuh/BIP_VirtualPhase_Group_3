within gantry_system;

model trolley_pendulum
  type Length = Real(unit="m");
  type Velocity = Real(unit="m/s");
  type AngularDisp = Real(unit="rad");
  type AngularVelo = Real(unit="rad/s");
  type Mass = Real(unit="kg", min=0);
  type Damping = Real;
  type Acceleration = Real(unit="m/s2");
  type ControlSignal = Real;

  parameter Mass m=200 "Mass of pendulum bob/container";
  parameter Mass M=10 "Mass of trolley/cart";
  parameter Length r=1 "Length of the rope connecting the pendulum bob to the trolley";
  parameter Damping d_p=0.05 "Damping factor swinging of pendulum";
  parameter Damping d_c=4.79 "Damping factor for motion of cart";
  parameter Acceleration g=9.8 "Constant for gravitational acceleration on the surface of the Earth (not Newton's gravitational constant!!)";
  
  // Variables
  Length x "Displacement of the trolley/cart";
  Velocity v "Velocity of the trolley/cart";
  AngularDisp theta "Angular displacement of the pendulum, w.r.t the trolley";
  AngularVelo omega "Angular velocity of the pendulum";
  ControlSignal u "Control signal to move the trolley and pendulum";

initial equation
  x = 0;
  v = 0;
  theta = 0;
  omega = 0;

equation
  der(x) = v;
  der(theta) = omega;
  der(v) = ( r*(d_c*v - m*(g*sin(theta)*cos(theta) + r*sin(theta)*omega^2) - u) - (d_p*cos(theta)*omega) ) / ( -r*(M+m*sin(theta)^2) );
  der(omega) = ( (d_p*omega*(m+M)) + (m^2*r^2*sin(theta)*cos(theta)*omega^2) + m*r*( (g*sin(theta)*(m+M) + ( cos(theta)*(u-d_c*v)))) ) / ( (m*r^2)*(-M-(m*sin(theta)^2)) );

//  u = 0;

  if time < 0.5 then
    u = 1000;
  else
    u = 0;
  end if;

end trolley_pendulum;