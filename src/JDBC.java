import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import com.microsoft.sqlserver.jdbc.*;

public class JDBC {
      public static void main(String[] args) {
            String cs = "jdbc:sqlserver://10.242.128.89:1433;"
                    + "database=LSDM;"
                    + "user=cloader;"
                    + "password=sw=jeth7bubuHa";
            Connection c = null;
            String query = args[0];
            try {
                c = DriverManager.getConnection(cs);
                Statement st = c.createStatement();
                st.execute(query);
                ResultSet rs = st.getResultSet();
                while (rs.next()) {
                    System.out.println(rs.getString(1));
                }
            }
            catch (Exception e) {
                e.printStackTrace();
            }
            finally {
                if (c != null) try {
                    c.close();
                } catch (Exception e) {
                }
            }
        }

    }
