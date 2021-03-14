import simplenode;

settings.tex="xelatex";
usepackage("mathpazo");
settings.outformat = "eps";

real u = 2cm;
pen text = white;
pen starttext = black;
currentpen = linewidth(0.8) + fontsize(9pt);
pen col = deepgreen;
draw_t Initial = none;
draw_t State = compose(filldrawer(col, darkgreen+0.6));
draw_t Accepting = compose(filler(col),
                           drawer(darkgreen+1.8), drawer(white+0.6));
draw_t Starting = compose(filler(red),
                           drawer(darkgreen+1.8), drawer(white+0.6));


node qa = Circle("$A$", u*dir(210), text, State),
     qb = Circle("$B$", u*dir(-30), text, State),
     qc = Circle("$C$", u*dir(90), text, State);

draw(qa.pos -- qb.pos);
draw(qb.pos -- qc.pos);
draw(qc.pos -- qa.pos);

draw(qa.pos -- qa.pos + 0.6*u*E, Arrow(7));
draw(qa.pos -- qa.pos + 0.6*u*N, Arrow(7));
draw(qb.pos -- qb.pos + 0.6*u*E, Arrow(7));
draw(qb.pos -- qb.pos + 0.6*u*N, Arrow(7));
draw(qc.pos -- qc.pos + 0.6*u*E, Arrow(7));
draw(qc.pos -- qc.pos + 0.6*u*N, Arrow(7));

draw(qa, qb, qc);

label("$q_1$", qa.pos + 0.5*u*E + 0.15u*S);
label("$q_2$", qa.pos + 0.5*u*N + 0.15u*W);

label("$q_3$", qb.pos + 0.5*u*E + 0.15u*S);
label("$q_4$", qb.pos + 0.5*u*N + 0.15u*E);

label("$q_5$", qc.pos + 0.5*u*E + 0.15u*S);
label("$q_6$", qc.pos + 0.5*u*N + 0.15u*W);

shipout(bbox(xmargin=0.3cm, ymargin=0.2cm, FillDraw(fillpen=white, drawpen=white)));
