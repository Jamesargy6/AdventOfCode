import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class day2 {

	public static void main(String[] args) {
		
		int totalPaperSqFt = 0;
		int totalRibbon = 0;
		int[] dim = new int[3];
		
		String fileName = args[0];
		try {
			FileReader reader = new FileReader(fileName);
			BufferedReader bReader = new BufferedReader(reader);
			String line;
			String[] rawDim = new String[3];
			while((line = bReader.readLine())!= null)
			{
				rawDim = line.split("x");
				for(int i = 0; i < rawDim.length; i++)
				{
					dim[i] = Integer.parseInt(rawDim[i]);
				}
				totalPaperSqFt += getWrappingPaper(dim);
				totalRibbon += getRibbon(dim);
			}
			
		
		
		}catch(FileNotFoundException ex) {
            System.out.println(
                    "Unable to open file '" + 
                    fileName + "'");                
            } catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		System.out.println("Total square footage: " + totalPaperSqFt + ", Total Ribbon: " + totalRibbon);

	}
	public static int getWrappingPaper(int[] dim)
		{
			int amt = 0;
			int w = dim[0], h = dim[1], l = dim[2];
			
			amt += 2*w*h + 2*w*l + 2*h*l;
			
			Arrays.sort(dim);
			amt += dim[0]*dim[1];
			
			return amt;
		}
		
	public static int getRibbon(int[] dim)
		{
			int amt = 0;
			Arrays.sort(dim);
			amt += dim[0]*dim[1]*dim[2];
			amt += 2*dim[0] + 2*dim[1];
			
			return amt;
		}

}
