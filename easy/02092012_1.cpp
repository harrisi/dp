#include <iostream>
#include <fstream>

std::string prompt(std::string ask) {
  std::string res;
  std::cout << ask;
  std::cin >> res;
  return res;
}

int main() {
  std::string name = prompt("Name? ");
  std::string age = prompt("Age? ");
  std::string uname = prompt("Username? ");
  
  std::string outs = "Your name is " + name + ", you are " + age +
    " years old, and your username is " + uname + ".\n";


  std::cout << outs; 
  std::ofstream f("out.log", std::ios_base::app);
  if (!f) {
    std::cerr << "error opening file";
    return 1;
  }
  f << outs;
}
