import java.util.Scanner;

class pruebaGit{
    public static void main(String[] args){
        System.out.println("This is Java");
        
        Scanner scanner = new Scanner(System.in);
        
        try {
            System.out.print("Ingrese el primer número: ");
            double numero1 = scanner.nextDouble();

            System.out.print("Ingrese el segundo número: ");
            double numero2 = scanner.nextDouble();

            System.out.print("Ingrese la operación (+, -, *, /): ");
            String operacion = scanner.next();

            double resultado = 0;

            switch (operacion) {
                case "+":
                    resultado = numero1 + numero2;
                    break;
                case "-":
                    resultado = numero1 - numero2;
                    break;
                case "*":
                    resultado = numero1 * numero2;
                    break;
                case "/":
                    resultado = numero1 / numero2;
                    break;
                default:
                    System.out.println("Operación no válida");
                    return;
            }

            System.out.println("El resultado es: " + resultado);
        } catch (Exception e) {
            System.out.println("Ha ocurrido un error. Por favor, asegúrese de ingresar números válidos.");
        } finally {
            scanner.close();
        }
    }
}




    