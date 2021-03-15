#version 3.7;

global_settings {
  assumed_gamma 1.0
}

#include "colors.inc"
#include "math.inc"

background { White }

#declare edgeRad = 0.002;
#declare num_segments = 20;
#declare edgeCol = Yellow;
#declare facefilter = 0.5;
#declare faceCol = White*0.6;
#declare faceColDimmed = faceCol * 0.3;

#declare edgeFinish = finish {
  ambient 0.2 diffuse 0.5 reflection 0.1 specular 0.6 roughness 0.01
}

#declare faceFinish = finish {
  ambient 0.5 diffuse 0.5 specular 0.6 roughness 0.005
}

#macro faceTexture(ind, faceType)
  #if(faceType)
    #local col = faceCol;
  #else
    #local col = faceColDimmed;
  #end

  texture {
    pigment { col filter facefilter }
    finish { faceFinish }
  }
#end

// return the normal vector of a 3d plane passes through the
// projected points of two 4d vectors p1 and p2
#macro get_clipping_plane(p1, p2)
    #local p12 = vnormalize(p1+p2);
    VPerp_To_Plane(p1-p12, p2-p12)
#end

// compute the signed distance of a vector to a plane,
// all vectors here are in 3d.
#macro distance_point_plane(p, p0, pnormal)
    vdot(p-p0, pnormal) / vlength(pnormal)
#end

// check if a vectors p is in the halfspace defined
// by the plane passes through p0 and has orientation pNormal.
#macro on_same_side(p, p0, pnormal)
    #local result = false;
    #local innprod = vdot(pnormal, p-p0);
    #if (innprod > 0)
        #local result = true;
    #end
    result
#end

// height of the upper plane sheet
#declare K = 4;

#macro FundCone(ht)
  #local num = 3;
  #local a = 2 / sqrt(3);
  #local pts = array[3] {
    <0, 0, K>,
    <1, 1/sqrt(3), K>,
    <1, -1/sqrt(3), K>
  };
  #local rib = 0;
  #local ind = 0;
  #while (ind < num)
    #local rib = rib + pts[ind];
    #local ind = ind+1;
  #end
  #local rib = vnormalize(rib);

  #local ind = 0;
  #local planes = array[num];
  #local dists = array[num];
  #local sides = array[num];
  #while (ind < num)
    #local ind2 = ind + 1;
    #if (ind2 = num)
      #local ind2 = 0;
    #end
    #local planes[ind] = get_clipping_plane(pts[ind], pts[ind2]);
    #local dists[ind] = distance_point_plane(0, pts[ind], planes[ind]);
    #local sides[ind] = on_same_side(rib, pts[ind], planes[ind]);
    #if (sides[ind] != true)
      #local planes[ind] = -planes[ind];
    #end
    #local ind = ind+1;
  #end
  intersection {
    sphere { 0, 1000 }
    #local ind = 0;
    #while (ind < num)
      plane { -planes[ind], dists[ind] }
      #local ind = ind+1;
    #end
    plane { z, ht }
    pigment { color Red }
    finish {
      ambient 0.3 diffuse 0.8 specular 0.2 roughness 0.2
    }
  }
#end

camera {
  location <0, -4, 2.8> * 3
  look_at <0, 0, 1>
  sky z
  up z
  right x*image_width/image_height
}

light_source {
  <3, -1, 20>
  color rgb 1.33
  area_light
  x*8 y*8
  5, 5
  jitter
  orient
  adaptive 2
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
  plane {
    <0, 0, 1>, K
    texture{ pigment { Background_color filter 0.5 } }
    texture{ Raster(RasterScale, RasterHalfLine) }
    texture{ Raster(RasterScale, RasterHalfLine) rotate<0, 0, 60> }
    texture{ Raster(RasterScale, RasterHalfLine) rotate<0, 0, 120> }
  }
#end

#declare AA = 5;
#declare BB = AA;
#declare uppersheet =  object {
  Grid(1, 0.025, White*1.3)
  clipped_by { plane { x  AA }}
  clipped_by { plane { -x  AA }}
  clipped_by { plane { y  BB }}
  clipped_by { plane { -y  BB }}
};

union{
  object { uppersheet }
  FundCone(6)
}

box {
  <-AA, -BB, -0.0001>, <AA, BB, 0.0001>
   texture {
     pigment { color Quartz }
     finish { ambient 0.5 diffuse 0.5 }
   }
}

sphere {
  <0, 0, 0>, 0.15
  pigment { color rgb <0.5, 1, 0> }
  finish { diffuse 0.5 ambient 0.3 specular 0.2 roughness 0.025 }
}
