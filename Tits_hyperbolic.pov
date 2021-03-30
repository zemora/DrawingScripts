#version 3.7;

#include "colors.inc"
#include "textures.inc"
#include "transforms.inc"

global_settings {
  assumed_gamma 1.0
}

background { Quartz }

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

#declare m1 = <1, 0, 0>;
#declare m2 = <-cos(pi/7), sin(pi/7), 0>;
#declare X = -cos(pi/3) / m2.y;
#declare m3 = <0, X, -sqrt(X*X-1)>;
#declare A = vcross(m2, m3);
#declare B = vcross(m3, m1);
#declare C = vcross(m1, m2);

#macro FundCone(ht)
  #local num = 3;
  #local pts = array[3] { A, B, C };
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
    finish { ambient 0.3 diffuse 0.8 specular 0.2 roughness 0.2 }
  }
#end

#declare projx = function (x,y,z) { x/(z+1) }
#declare projy = function (x,y,z) { y/(z+1) }

#declare ImageFn = function {
  pigment {
    image_map { png "73.png" once }
    translate <-.5, -.5, 0>
  }
}

#declare trans = 0.4;
#declare PigmentR = pigment {
  function { ImageFn(projx(x,y,z)/2, projy(x,y,z)/2, 0).red }
  color_map {
    [ 0 color rgbt <0, 0, 0, trans>]
    [ 1 color rgbt <3, 0, 0, trans> ]
  }
}

#declare PigmentG = pigment {
  function { ImageFn(projx(x,y,z)/2, projy(x,y,z)/2 ,0).green }
  color_map {
    [ 0 color rgbt <0, 0, 0, trans>]
    [ 1 color rgbt <0, 3, 0, trans> ]
  }
}

#declare PigmentB = pigment {
  function { ImageFn(projx(x,y,z)/2, projy(x,y,z)/2 ,0).blue }
  color_map {
    [ 0 color rgbt <0, 0, 0, trans>]
    [ 1 color rgbt <0, 0, 3, trans> ]
  }
}

#declare hyperboloid = object {
  poly {
    2, <1, 0, 0, 0, 1, 0, 0, -1, 0, 1>
  }
  clipped_by { plane{-z, 0 } }
  clipped_by { plane{ z, 2 } }
  texture {
    pigment {
      average
      pigment_map {
        [ PigmentR ]
        [ PigmentG ]
        [ PigmentB ]
      }
    }
    finish {
      ambient 0.7
      diffuse 0.3
      reflection 0
      specular 0.2
      roughness 0.2
      irid { 0.3 thickness 0.2 turbulence 0.05 }
      conserve_energy
    }
  }
}

#declare lightcone = object {
  poly {
    2, <1, 0, 0, 0, 1, 0, 0, -1, 0, 0>
  }
  clipped_by{ plane{-z, 0} }
  clipped_by{ plane{ z, 2} }
  pigment { Pink transmit 0.3 }
  finish {
    ambient 0.8
    diffuse 0.2
    reflection 0
    roughness 0.25
    irid { 0.3 thickness 0.2 turbulence 0.05 }
    conserve_energy
  }
}

object{ hyperboloid }
object { lightcone }
plane {
  z, 0
  pigment {
    image_map { png "73.png" once }
    translate <-0.5, -0.5, 0>
    scale 4
  }
  finish {
    ambient 0.3 diffuse 0.7 reflection 0 roughness 0.25
  }
}

FundCone(2.5)

camera {
  location <-3, -3, 4>
  look_at <0, 0, 0.5>
  sky z
  up z
  right x*image_width/image_height
}

light_source {
  <-10, 10, 6>
  color rgb 1
  area_light
  x*4 y*4
  5, 5
  jitter
  orient
  adaptive 2
}
