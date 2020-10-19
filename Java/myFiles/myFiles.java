/*
Harjaspreet Bhangu
Oct, 19 2020
To: Mr.Bains
Program that interacts with different methods
*/


//Import for user input
import java.util.Scanner;

//My class named myFiles
public class myFiles{
  double file;

//fileTest method for giving the variable file a value
  public double fileTest(double fileSize) {
    file = fileSize;
    return file;
  }
  
//importFile method for testing to see if the file size is right for import
  public void importFile() {
      if (file <= 26.00) {
//If true, then print out the statement below
      System.out.println("File is ready for import");
    } else {
//If false then print out the statement below
      System.out.println("Your file size should be 26MB or lower.");
    }
  }

//main Method
  public static void main(String args[]) {
//Defining labReport so it can interact with all public methonds
    myFiles labReport = new myFiles();

//Defining input for the user input
    Scanner input = new Scanner(System.in);

//assigning dNum so it can hold the user input
    double dNum;
    dNum = input.nextDouble();

//User input    
    labReport.fileTest(dNum);
    labReport.importFile();

//Closing userinput  
    input.close();
  }
}