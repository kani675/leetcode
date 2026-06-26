int mySqrt(int x) {
    double i=1;
    while(i*i<x){i++;}
    if(i*i!=x)i--;
    return i;
}