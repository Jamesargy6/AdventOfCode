import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class day1 {

	public static void main(String[] args) {
		
		int floor = 0;
		int currentPos = 1;
		int basePos = 0;
		String fileName = args[0];
		
		try {
			FileReader reader = new FileReader(fileName);
			BufferedReader bReader = new BufferedReader(reader);
			String line;
			while((line = bReader.readLine())!= null)
			{
				for(char nextIns : line.toCharArray())
				{
					floor +=(nextIns=='(')?1:-1;
					if(floor==-1 && basePos == 0)
					{
						basePos = currentPos;
					}
					currentPos++;
				}
			}
			
		
		
		}catch(FileNotFoundException ex) {
            System.out.println(
                    "Unable to open file '" + 
                    fileName + "'");                
            } catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		System.out.println("Result: " + floor + ", basePos: " + basePos);

	}

}
