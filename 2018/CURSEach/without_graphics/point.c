#include <stdio.h>
#include <stdlib.h>
#include "point.h"
#include <math.h>

point* point_arr_init(unsigned size){
    point* a =(point*)malloc(sizeof(point)*size);
    return a;
}

Line* Line_arr_init(unsigned size){
    Line* a =(Line*)malloc(sizeof(Line)*size);
    return a;
}

int point_rotate(point a,point b, point c){
    return ((b.x-a.x)*(c.y-b.y)-(b.y-a.y)*(c.x-b.x));
}

double Line_lenght(Line a){
    return sqrt((a.b.x-a.a.x)*(a.b.x-a.a.x)+(a.b.y-a.a.y)*(a.b.y-a.a.y));
}

int point_to_Line_lenght(Line l, point p){
    return (abs(((l.b.y-l.a.y)*p.x)-((l.b.x-l.a.x)*p.y)+l.b.x*l.a.y-l.b.y*l.a.x)/sqrt((l.b.y-l.a.y)*(l.b.y-l.a.y)+(l.b.x-l.a.x)*(l.b.x-l.a.x))
}


int Line_intersect(Line a,Line b){
  return ((point_rotate(a.a,a.b,b.a)*point_rotate(a.a,a.b,b.b))<=0)&&((point_rotate(b.a,b.b,a.a)*point_rotate(b.a,b.b,a.b))<0);
}

void point_to_Line_arr(point* orig,Line* dest,unsigned size){
    Line temp_Line;
    int i;
    for(i=0;i<size-1;i++){
        temp_Line.a=orig[i];
        temp_Line.b=orig[i+1];
        dest[i]=temp_Line;
    }
    temp_Line.a=orig[0];
    temp_Line.b=orig[i];
    dest[i]=temp_Line;
}

void Line_to_point_arr(Line* orig,point* dest,unsigned size){
    dest[0]=orig[0].a;
    for(int i=0;i<size-1;i++){
        dest[i+1]=orig[i].b;

    }
}

void point_read_arr(point *arr,int size){
  printf("Input point coordinates - ");
  for(int i=0;i<size;i++){
      scanf("%d:%d",&arr[i].x,&arr[i].y);
  }
}

void point_write_arr(point *arr,int size){
    for (int i=0;i<size;i++){
        print_point(arr[i]);
    }
    printf("\n");

}

void print_point(point a){
    printf("%d:%d ",a.x,a.y);
}

void print_Line(Line a){
    printf("\n");
    print_point(a.a);
    print_point(a.b);
    printf("\n");

}

double Line_point_sub(Line l,point p){
    Line temp_Line1,temp_Line2;
    temp_Line1.a=l.a;
    temp_Line1.b=p;
    temp_Line2.a=p;
    temp_Line2.b=l.b;
    return (Line_lenght(temp_Line1)+Line_lenght(temp_Line1)-Line_lenght(l))
}

void Line_arr_delete(Line* arr,int *size,int pos){
    switch (pos) {
        case *size-1: *size--;
        break;
        default: for(int i=pos;i++;i<*size)
        arr[pos]=arr[pos+1];
    }
}

void Line_write_arr(Line* arr,int size){
  for (int i=0;i<size;i++){
      print_Line(arr[i]);
    }
}
