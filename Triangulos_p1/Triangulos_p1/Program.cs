int ladoA = GetValidNumber("Escribe el primer lado del triángulo:");
int ladoB = GetValidNumber("Escribe el segundo lado del triángulo:");
int ladoC = GetValidNumber("Escribe el tercer lado del triángulo:");


if (ladoA == ladoB || ladoB == ladoC || ladoA == ladoC)
{
    Console.WriteLine("El triángulo es isósceles.");
}
else if (ladoA == ladoB && ladoB == ladoC)
{
    Console.WriteLine("El triángulo es equilátero.");
}
else
{
    Console.WriteLine("El triángulo es escaleno.");
}

int GetValidNumber(string prompt)
{
    int number;
    while (true)
    {
        Console.WriteLine(prompt);
        if (int.TryParse(Console.ReadLine(), out number))
        {
            return number;
        }
        else
        {
            Console.WriteLine("Por favor, introduce un número válido.");
        }
    }
}