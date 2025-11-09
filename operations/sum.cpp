#include<iostream>
using namespace std;


extern "C"{
    
    int sum(int a, int b){

    int sum = a + b;

    return sum;
    }
}