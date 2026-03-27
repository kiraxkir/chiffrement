package database;



import service.User;

import java.sql.*;

import static java.time.chrono.JapaneseEra.values;

public class UserDB {

    public boolean userExists(User user) {
        String verifie = "SELECT * FROM users WHERE telephone = ? AND nom = ?";

        try (Connection co = DbConnection.getConnection();
             PreparedStatement ps = co.prepareStatement(verifie)) {

            ps.setString(1, user.getTelephone());
            ps.setString(2, user.getNom());

            ResultSet rs = ps.executeQuery();

            return rs.next(); // true si trouvé, false sinon

        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }

    public boolean createUser(User user) {
        String query = "INSERT INTO users(nom, prenom, telephone, mot_de_passe) VALUES (?,?,?,?)";

        if (userExists(user)) {
            System.out.println("cet utilisateur existe");
            return false;
        } else {
            try (Connection co = DbConnection.getConnection();
                 PreparedStatement ps = co.prepareStatement(query)) {

                ps.setString(1, user.getNom());
                ps.setString(2, user.getPrenom());
                ps.setString(3, user.getTelephone());
                ps.setString(4, user.getMdp());

                int rows = ps.executeUpdate();

                if (rows > 0) {
                    System.out.println("Enregistrement reussi !!!!");
                    return true;
                } else {
                    return false;
                }

            } catch (SQLException e) {
                e.printStackTrace();
                return false;
            }
        }
    }

}


