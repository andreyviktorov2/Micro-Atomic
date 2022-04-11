#include <chrono>
#include <iostream>
#include <thread>

#define CURRENT_VERSION 1

int main() {
  std::cout
      << "Micro Atomic research project.\nAll rights are reserved. Version "
      << CURRENT_VERSION << "\n";
  std::cout << "\n\nPlease, enter the name of the file you want to open. Supported "
               "formats are png, jpg.\n";

  std::string dummy;
  std::cin >> dummy;

  std::cout << "\n--Processing file " << dummy << "\n";
  std::this_thread::sleep_for(std::chrono::seconds(1));
  std::cout
      << "File processed succesfully! Data was read, the file is closed\n\n";

  std::cout << "Do You want to save full report to the file? (Y/n)\n";
  char answer;
  std::cin >> answer;
  if (answer == 'Y') std::cout << "Report will be saved in FullReport.format\n";

  std::cout
      << "Neural network started working. Please, wait until it finishes.\n\n";
  std::this_thread::sleep_for(std::chrono::seconds(2));

  std::cout << "Network finished its work. "
            << (answer == 'Y' ? "You can see full report in FullReport.format\n"
                              : "\n");
  std::cout << "\nReport for the result of network work:\n";
  std::cout << 2 << " items was found\n";
}
