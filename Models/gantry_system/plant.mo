within gantry_system;

block plant

  extends trolley_pendulum;
  extends Modelica.Blocks.Icons.Block;

  Modelica.Blocks.Interfaces.RealInput u_input "Input signal connector" annotation(
    Placement(transformation(origin = {-120, 0}, extent = {{-20, -20}, {20, 20}})));
  Modelica.Blocks.Interfaces.RealOutput x_output "Output signal connector" annotation(
    Placement(transformation(origin = {110, 0}, extent = {{-10, -10}, {10, 10}})));

equation
  u_input = u;


end plant;