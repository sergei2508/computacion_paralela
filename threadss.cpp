#include <iostream>
#include <thread>

int main() {
    unsigned int num_threads = std::thread::hardware_concurrency();

    if (num_threads == 0) {
        std::cout << "No se pudo determinar el número de hilos disponibles.\n";
    } else {
        std::cout << "Número de hilos disponibles en tu computadora: " << num_threads << "\n";
    }

    return 0;
}