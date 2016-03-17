#include <iostream>

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
  
  std::cout << "\nYour name is " << name << ", you are " << age <<
    " years old, and your username is " << uname << ".\n";
}
