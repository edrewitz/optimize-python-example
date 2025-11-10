#include<iostream>
using namespace std;


extern "C"{
    
    int sum(int a, int b){

        /*
        Function that adds integers a and b in C++
        */

    int sum = a + b;

    return sum;
    }
}