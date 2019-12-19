-- Lua script.
p=tetview:new()
p:load_mesh("C:/Users/flobo/Documents/Gits/PD3D/damo/arch_3_s10.ele")
rnd=glvCreate(0, 0, 500, 500, "TetView")
p:plot(rnd)
glvWait()
