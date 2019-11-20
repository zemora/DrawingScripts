#version 3.7;

#include "colors.inc"
#include "transforms.inc"

global_settings {
    assumed_gamma 1.0
}


#macro Raster(RScale, RLine)
    pigment {
        gradient x scale RScale
        color_map {
            [0.000   color rgb  <1,1,1>*0.1]
            [0+RLine color rgb  <1,1,1>*0.3]
            [0+RLine color rgbt <1,1,1,1>]
            [1-RLine color rgbt <1,1,1,1>]
            [1-RLine color rgb  <1,1,1>*0.3]
            [1.000   color rgb  <1,1,1>*0.5]
        }
    }
#end


#macro Grid(RasterScale, RasterHalfLine, Background_color)
    plane{
        <0,0,1>, 0
        texture{ pigment {Background_color transmit 0.7 } }
        texture{ Raster(RasterScale, RasterHalfLine) }
        texture{ Raster(RasterScale, RasterHalfLine) rotate<0,0,90> }
    }
#end


object {
    Grid(0.50, 0.035, White*1.5)
}


#macro Axis_(AxisLen, Dark_Texture, Light_Texture) 
    union{
        cylinder {
            <0, -AxisLen, 0>, <0, AxisLen, 0>, 0.03
            texture{
                checker 
                texture{ Dark_Texture } 
                texture{ Light_Texture}
                scale 0.2
                translate<0.1, 0, 0.1>}
        }
        cone{
            <0, AxisLen, 0>, 0.05, <0, AxisLen+0.5, 0>, 0
            texture{ Dark_Texture }
        }
    }
#end


#macro AxisXYZ(AxisLenX, AxisLenY, AxisLenZ, Tex_Dark, Tex_Light)
    union{
        #if (AxisLenX != 0)
            object {
                Axis_(AxisLenX, Tex_Dark, Tex_Light)
                rotate<0, 0, -90>
            }
            text {
                ttf "arial.ttf", "x", 0.15, 0
                texture{ Tex_Dark } 
                scale 0.4
                rotate 90*z
                translate <AxisLenX + 0.05, -0.4, 0.10>
            }
        #end
        #if (AxisLenY != 0)
            object {
                Axis_(AxisLenY, Tex_Dark, Tex_Light)
                rotate<0, 0, 0>
            }
            text {
                ttf "arial.ttf", "y", 0.15, 0
                texture{ Tex_Dark }    
                scale 0.4
                rotate 90*z
                translate <-0.3, AxisLenY-0.20, 0.10>
            }
        #end
        #if (AxisLenZ != 0)
            object {
                Axis_(AxisLenZ, Tex_Dark, Tex_Light)
                rotate<90, 0, 0>
            }
            text {
                ttf "arial.ttf", "z", 0.15, 0
                texture{ Tex_Dark }
                scale 0.4
                rotate <90, 0, 90>
                translate <0.15, 0.2, AxisLenZ+0.30>
            }
        #end
    }
#end

#macro mirror(v1, v2, col, c1, c2)
    object {
           box {
               <-c1, -c2, -0.0001>, <c1, c2, 0.0001>
               texture {
                   pigment{ color col transmit 0.5 }
                   finish {diffuse .5 ambient .1 reflection 0 phong 1}
                       }               
               }
     no_shadow
     rotate v1
     rotate v2
    }
#end


#declare FIN = finish {
    ambient 0.4
    diffuse 0.5
    reflection 0.1
    specular 3
    roughness 0.003
}

#declare Texture_A_Dark  = texture {
    pigment{ color rgb <1, 0.45, 0>}
    finish { FIN }
}

#declare Texture_A_Light = texture { 
    pigment{ color rgb <1, 1, 1>}
    finish { FIN }
}

object{
    AxisXYZ(3.6, 4.5, 5, Texture_A_Dark, Texture_A_Light)
}

#declare rad = 0.15;

#macro Vert(vs, k, ind)
    sphere {
        vs[ind], 0.04
        texture {
            pigment { #if (ind=0) Magenta #else SkyBlue #end }
            finish { ambient 0.2
    diffuse 0.5
    reflection 0.1
    specular 0.6
    roughness 0.01
 }
        }
    }
#end


#macro Edge(vs, i, v1, v2)
    cylinder {
        vs[v1], vs[v2], 0.02
        texture {
            pigment { color Orange }
            finish { ambient 0.2
    diffuse 0.5
    reflection 0.1
    specular 0.6
    roughness 0.01
 }
        }
    }
#end

#declare sca = 3.3;
union {
 #include "data.inc"
 scale sca
}


#declare height = vertices[0].z;

mirror(90*y, 0, Red, height*sca, 4)
mirror(90*y, 144*z, Green, height*sca, 4)
mirror(60*x, 0, SteelBlue, 4, sca*vlength(< vertices[0].z,  vertices[0].y>))


camera {
    location <1, 0.2, 2.2> * 4.2
    look_at <0, 0, 0>
    sky z
    up z
    right x*image_width/image_height
}

light_source {
    <1, 0.5, 1> * 10
    color rgb 1.33
    area_light
    x*8 y*8
    5, 5
    jitter
    orient 
    adaptive 2
}
