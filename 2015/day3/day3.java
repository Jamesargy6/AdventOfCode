import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

import java.util.Hashtable;


public class day3 {

	public static void main(String[] args) {

		int uniqueHouses = 1;
		int currentX = 0;
		int currentY = 0;
		int currentRoboX = 0;
		int currentRoboY = 0;
		
		String fileName = args[0];
		Hashtable<Integer,Hashtable<Integer,Integer>> houseGrid = new Hashtable<Integer,Hashtable<Integer,Integer>>();
		houseGrid.put(0,new Hashtable<Integer,Integer>());
		houseGrid.get(0).put(0,1);
		try {
			FileReader reader = new FileReader(fileName);
			BufferedReader bReader = new BufferedReader(reader);
			String line;
			String[] rawDim = new String[3];
			boolean santa = true;
			while((line = bReader.readLine())!= null)
			{
				for(char nextIns : line.toCharArray())
				{
					if(santa)
					{
						switch(nextIns)
						{
							case '^':
								currentY++;
								break;
							case 'v':
								currentY--;
								break;
							case '>':
								currentX++;
								break;
							case '<': 
								currentX--;
								break;
						}
								
						if(houseGrid.get(currentX) != null)
						{
							if(houseGrid.get(currentX).get(currentY) != null)
							{
								houseGrid.get(currentX).put(currentY,houseGrid.get(currentX).get(currentY));
							}
							else
							{
								houseGrid.get(currentX).put(currentY, 1);
								uniqueHouses++;
							}
						}
						else
						{
							houseGrid.put(currentX, new Hashtable<Integer,Integer>());
							houseGrid.get(currentX).put(currentY, 1);
							uniqueHouses++;
						}
					}
					else
					{
						switch(nextIns)
						{
							case '^':
								currentRoboY++;
								break;
							case 'v':
								currentRoboY--;
								break;
							case '>':
								currentRoboX++;
								break;
							case '<': 
								currentRoboX--;
								break;
						}
								
						if(houseGrid.get(currentRoboX) != null)
						{
							if(houseGrid.get(currentRoboX).get(currentRoboY) != null)
							{
								houseGrid.get(currentRoboX).put(currentRoboY,houseGrid.get(currentRoboX).get(currentRoboY));
							}
							else
							{
								houseGrid.get(currentRoboX).put(currentRoboY, 1);
								uniqueHouses++;
							}
						}
						else
						{
							houseGrid.put(currentRoboX, new Hashtable<Integer,Integer>());
							houseGrid.get(currentRoboX).put(currentRoboY, 1);
							uniqueHouses++;
						}
						
						System.out.println("Santa coords: (" + currentX + ", " + currentY + "), Current RoboSanta Coords: (" + currentRoboX + ", " + currentRoboY + ")");
					}
					santa = !santa;		
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
		
		System.out.println("# of Unique houses visited: " + uniqueHouses);

	}
	

}
