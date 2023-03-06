#include<stdio.h>
#include<math.h>
#include<string.h>
#include<unistd.h>
float a, b,c;

float cubewigth=10;
int wigth=160,height=44;
float zBuffer[160*44];
char buffer[160*44];
int backgroundASCIICode=' ';
float K1=40;

int distanceFromCam=60;
float incrementSpeed=0.6;

float x, y,z;

float ooz;
int  xp, yp;
int idx;

float calculateX(int i, int j , int k){
    return j*sin(a)*sin(b)*cos(c)-k*cos(a)*sin(b)*cos(c)+j*cos(a)*sin(c)+k*sin(a)*sin(c)+i*cos(b)*cos(c);
}

float calculateY(int i, int j, int k){
    return j*cos(a)*cos(c)+k*sin(a)*cos(c)-j*sin(a)*sin(b)*sin(c)+ k*cos(a)*sin(b)*sin(c)-i*cos(b)*sin(c);
}

float calculateZ(int i, int j ,int k){

  return k*cos(a)*cos(b)-j*sin(a)*cos(b)+i*sin(b);

}
void calculateForSurface(float cubeX, float cubeY, float cubeZ,int ch){
    x=calculateX(cubeX,cubeY,cubeZ);
    y=calculateX(cubeX,cubeY,cubeZ);
    z=calculateX(cubeX,cubeY,cubeZ)+distanceFromCam;

    ooz=1/z;
    xp=(int)(wigth/2+K1*ooz*x*2);
    yp=(int)(height/2+K1*ooz*y);

    idx=xp+yp*wigth;

    if(idx>=0 && idx<wigth){
        if(ooz>zBuffer[idx]){
            zBuffer[idx]=ooz;
            buffer[idx]=ch;
        }
    }
}

int main(){
    printf("\x1b[2J");

    while(1){
        memset(buffer , backgroundASCIICode, wigth*height);
        memset(zBuffer,0,wigth*height*4);
        for(float cubeX=-cubewigth; cubeX<cubewigth; cubeX+=incrementSpeed){
            for(float cubeY=-cubewigth; cubeY<cubewigth; cubeY+=incrementSpeed){
                calculateForSurface(cubeX,cubeY,-cubewigth,'#');
            }
        }
        printf("\x1b[H");

        for(int k=0;k< wigth*height; k++){
            putchar(k%wigth ? buffer[k]: 10);
        }
        a+=0.005;
        b+=0.005;
    }
    return 0;
}