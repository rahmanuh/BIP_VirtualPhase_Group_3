within gantry_system;

model exp_1_calib_damp_c
  type Length = Real(unit="m");
  type Velocity = Real(unit="m/s");
  type Mass = Real(unit="kg", min=0);
  type Damping = Real;

  parameter Mass M=10 "Mass of trolley/cart";
  parameter Damping d_c=2 "Damping factor for motion of cart";

  // Variables
  Length x "Displacement of the trolley/cart";
  Velocity v "Velocity of the trolley/cart";

initial equation
  x = 0;
  v = 5;
 
equation
  der(x) = v;
  der(v) = -(d_c/M) * v;

end exp_1_calib_damp_c;