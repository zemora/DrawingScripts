#version 3.7;

#include "colors.inc"

global_settings {
    assumed_gamma 1.0
}


#macro Raster(RScale, RLine)
    pigment {
        gradient x scale RScale
        color_map {
            [0.000   color rgb  <1,1,1>*0.5]
            [0+RLine color rgb  <1,1,1>*0.5]
            [0+RLine color rgbt <1,1,1,1>]
            [1-RLine color rgbt <1,1,1,1>]
            [1-RLine color rgb  <1,1,1>*0.5]
            [1.000   color rgb  <1,1,1>*0.5]
        }
    }
#end


#macro Grid(RasterScale, RasterHalfLine, Background_color)
    plane{
        <0,1,0>, 0
        texture{ pigment {Background_color } }
        texture{ Raster(RasterScale, RasterHalfLine) }
        texture{ Raster(RasterScale, RasterHalfLine) rotate<0,90,0> }
    }
#end


object {
    Grid(0.50, 0.035, White*1.1)
}


#macro Axis_(AxisLen, Dark_Texture, Light_Texture) 
    union{
        cylinder {
            <0, -AxisLen, 0>, <0, AxisLen, 0>, 0.05
            texture{
                checker 
                texture{ Dark_Texture } 
                texture{ Light_Texture}
                translate<0.1, 0, 0.1>}
        }
        cone{
            <0, AxisLen, 0>, 0.15, <0, AxisLen+0.7, 0>, 0
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
                scale 0.5
                translate <AxisLenX + 0.05, 0.4, -0.10>
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
                scale 0.5
                translate <-0.75,AxisLenY+0.50,-0.10>
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
                scale 0.5
                translate <-0.75, 0.2, AxisLenZ+0.10>
            }
        #end
    }
#end


#declare FIN = finish {
    ambient 0.2
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
    AxisXYZ( 4.5, 3.0, 5, Texture_A_Dark, Texture_A_Light)
}

#declare rad = 0.15;

torus {
    3, rad
    pigment { color Orange }
    finish {
        specular 0.6
        reflection 0.1
        roughness 0.02
        diffuse 0.6
        ambient 0.3
    }
    translate y*rad
}

camera {
    location <3, 3, -3> * 2
    look_at <0, 0, 0>
    sky y
    right x*image_width/image_height
}

light_source {
    <1, 1.4, 1> * 100
    color rgb 1.3
    area_light
    x*8 y*8
    3, 3
    jitter
    orient 
    adaptive 1
}
