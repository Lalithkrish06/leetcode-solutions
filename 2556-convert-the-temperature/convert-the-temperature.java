class Solution {
    public double[] convertTemperature(double celsius) {
      double ans=(double)(celsius+273.15);
      double ans1=(double)(celsius*1.80+32.00);
      return new double[]{ans,ans1};
    }
}