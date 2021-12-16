public class ExperimentalFarm
{
private Plot[][] farmPlots;
 
public ExperimentalFarm(Plot[][] p)
{
   this.farmPlots = p;
}
 
/** Returns the plot with the highest yield for a given crop type, as described in part (a). */
public Plot getHighestYield(String c)
{
  Plot plot = null;
  int highestYield = 0;
 
  for (int i = 0; i < 3; i++) {
     for (int j = 0; j < 2; j++) {
      if(farmPlots[i][j].getCropType().equals(c) && farmPlots[i][j].getCropYield() > highestYield) {
           highestYield = farmPlots[i][j].getCropYield();
           plot = farmPlots[i][j];
      }
   }
 }
   return plot;
}     
 
/** Returns true if all plots in a given column in the two-dimensional array farmPlots
* contain the same type of crop, or false otherwise, as described in part (b).
*/
public boolean sameCrop(int col)
{
boolean state = true;

  String crop = farmPlots[0][col].getCropType();

  for(int i=0;i<4;i++)

  {

     if(!farmPlots[i][col].getCropType().equals(crop))

        {

        state = false;

        }
}
return state;
}
}
