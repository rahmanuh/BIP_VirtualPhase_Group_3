within gantry_system;

block pid_controller_block

extends trolley_pendulum;
extends Modelica.Blocks.Icons.Block;
  Modelica.Blocks.Interfaces.RealInput u_input "Input signal connector";
  Modelica.Blocks.Interfaces.RealOutput x_output "Output signal connector";
  
  Modelica.Blocks.Math.Gain proportional_gain(k = k_p)  annotation(
    Placement(transformation(origin = {2, 64}, extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Continuous.Integrator integral(k = k_i)  annotation(
    Placement(transformation(origin = {0, 22}, extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Continuous.Derivative derivative(k = k_d)  annotation(
    Placement(transformation(origin = {0, -28}, extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Math.Add substract(k2 = -1)  annotation(
    Placement(transformation(origin = {-46, 22}, extent = {{-10, -10}, {10, 10}})));
   
  Modelica.Blocks.Math.MultiSum multiSum(nu = 3)  annotation(
    Placement(transformation(origin = {38, 22}, extent = {{-10, -10}, {10, 10}})));

  parameter Real k_p(start = 10);
  parameter Real k_i(start = 10);
  parameter Real k_d(start = 10);
equation
  u_input = trolley_pendulum.u;
  x_output = trolley_pendulum.x;
  connect(substract.y, proportional_gain.u) annotation(
    Line(points = {{-35, 22}, {-26, 22}, {-26, 64}, {-10, 64}}, color = {0, 0, 127}));
  connect(integral.u, substract.y) annotation(
    Line(points = {{-12, 22}, {-34, 22}}, color = {0, 0, 127}));
  connect(derivative.u, substract.y) annotation(
    Line(points = {{-12, -28}, {-26, -28}, {-26, 22}, {-34, 22}}, color = {0, 0, 127}));
  connect(proportional_gain.y, multiSum.u[1]) annotation(
    Line(points = {{13, 64}, {27, 64}, {27, 22}}, color = {0, 0, 127}));
  connect(integral.y, multiSum.u[2]) annotation(
    Line(points = {{11, 22}, {27, 22}}, color = {0, 0, 127}));
  connect(derivative.y, multiSum.u[3]) annotation(
    Line(points = {{11, -28}, {27, -28}, {27, 22}}, color = {0, 0, 127}));
end pid_controller_block;