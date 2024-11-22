within gantry_system;

model control_loop
  pid_block pid(k_p = 3, k_i = 2, k_d = 0)  annotation(
    Placement(transformation(origin = {-10, 16}, extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Math.Add subs(k2 = -1)  annotation(
    Placement(transformation(origin = {-52, 16}, extent = {{-10, -10}, {10, 10}})));
  Modelica.Blocks.Sources.Constant r(k = 20)  annotation(
    Placement(transformation(origin = {-88, 32}, extent = {{-10, -10}, {10, 10}})));
  plant process annotation(
    Placement(transformation(origin = {32, 16}, extent = {{-10, -10}, {10, 10}})));
equation
  connect(subs.y, pid.e_input) annotation(
    Line(points = {{-40, 16}, {-22, 16}}, color = {0, 0, 127}));
  connect(r.y, subs.u1) annotation(
    Line(points = {{-76, 32}, {-64, 32}, {-64, 22}}, color = {0, 0, 127}));
  connect(pid.u_output, process.u_input) annotation(
    Line(points = {{2, 16}, {20, 16}}, color = {0, 0, 127}));
  connect(process.x_output, subs.u2) annotation(
    Line(points = {{44, 16}, {64, 16}, {64, -40}, {-80, -40}, {-80, 10}, {-64, 10}}, color = {0, 0, 127}));
end control_loop;