within gantry_system;

block pid_block

  parameter Real k_p(start=1);
  parameter Real k_i(start=1);
  parameter Real k_d(start=1);

  Modelica.Blocks.Interfaces.RealInput e_input "Input signal connector" annotation(
    Placement(transformation(origin = {-120, 0}, extent = {{-20, -20}, {20, 20}})));
  Modelica.Blocks.Interfaces.RealOutput u_output "Output signal connector" annotation(
    Placement(transformation(origin = {110, 0}, extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Math.Gain proportional(k = k_p)  annotation(
    Placement(transformation(origin = {-12, 30}, extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Continuous.Integrator integral(k = k_i)  annotation(
    Placement(transformation(origin = {-12, 0}, extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Continuous.Derivative derivative(k = k_d)  annotation(
    Placement(transformation(origin = {-12, -34}, extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Math.Add3 add3 annotation(
    Placement(transformation(origin = {30, 0}, extent = {{-10, -10}, {10, 10}})));

equation

  connect(proportional.y, add3.u1) annotation(
    Line(points = {{0, 30}, {18, 30}, {18, 8}}, color = {0, 0, 127}));
  connect(integral.y, add3.u2) annotation(
    Line(points = {{0, 0}, {18, 0}}, color = {0, 0, 127}));
  connect(derivative.y, add3.u3) annotation(
    Line(points = {{0, -34}, {18, -34}, {18, -8}}, color = {0, 0, 127}));
  connect(add3.y, u_output) annotation(
    Line(points = {{42, 0}, {110, 0}}, color = {0, 0, 127}));
  connect(e_input, integral.u) annotation(
    Line(points = {{-120, 0}, {-24, 0}}, color = {0, 0, 127}));
  connect(proportional.u, e_input) annotation(
    Line(points = {{-24, 30}, {-44, 30}, {-44, 0}, {-120, 0}}, color = {0, 0, 127}));
  connect(derivative.u, e_input) annotation(
    Line(points = {{-24, -34}, {-44, -34}, {-44, 0}, {-120, 0}}, color = {0, 0, 127}));
end pid_block;