-- Lua script.
p=tetview:new()
p:load_mesh("C:/Users/flobo/Documents/Gits/PD3D/damo/input/v4/arch_4_s10.ele")
rnd=glvCreate(0, 0, 500, 500, "TetView")
p:plot(rnd)
glvWait()
