import java.io.*;
import java.util.*;

public class FollowDirections
{
  public static void main(String args[]) throws IOException
  {

    if(args.length != 1)
    { 
      System.out.println("ERROR: Please enter a file containing directions");
      return;
    }

    int dir = 1, x = 0, y = 0;

    File file = new File(args[0]);
    Scanner scan = new Scanner(file);

      
    while(scan.hasNext())
    {
      String line = scan.nextLine();

      String []direction = line.split(" ");
      
      if(direction[0].equals("Turn"))
      {
        if(direction[1].equals("right"))
        {
          if(dir == 4)
            dir = 1;
          else
            dir++;
        }

        else if(direction[1].equals("left"))
        {
          if(dir == 1)
            dir = 4;
          else
            dir--;
        }
        
        continue;
      }

      else if(direction[0].equals("Move"))
      {
        if(dir == 4)
          x -= Integer.parseInt(direction[1]);

        if(dir == 3)
          y -= Integer.parseInt(direction[1]);

        if(dir == 2)
          x += Integer.parseInt(direction[1]);

        else if(dir == 1)
          y += Integer.parseInt(direction[1]);
      }

      else
      {
        System.out.println("ERROR: File does not contain directions");
        return;
      }
    }

    System.out.println(x + "," + y);
  }
}