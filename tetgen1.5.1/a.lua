-- Lua script.
p=tetview:new()
p:load_mesh("D:/Google Drive/Projects/Deformation-based Fabrication Optimization/Software/damo/tetgen1.5.1/build/Debug/arch.1.ele")
rnd=glvCreate(0, 0, 500, 500, "TetView")
p:plot(rnd)
glvWait()
