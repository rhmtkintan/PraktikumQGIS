import shapefile
w=shapefile.Writer("soal10", shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("hay","satu")
w.record("hiy","dua")
w.record("huy","tiga")
w.record("hey","empat")
w.record("hoy","lima")
w.record("haiyu","enam")

w.poly([[[1,1], [4,1], [1,3], [1,1]]])
w.poly([[[5,1], [8,1], [8,3], [5,1]]])

w.poly([[[9,1], [12,1], [9,3], [9,1]]])
w.poly([[[4,4], [4,6], [1,6], [4,4]]])

w.poly([[[5,4], [8,6], [5,6], [5,4]]])
w.poly([[[12,4], [12,6], [9,6], [12,4]]])


w.close()