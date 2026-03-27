package org.example;


import database.UserDB;
import javafx.fxml.FXML;

import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.ButtonType;
import javafx.scene.control.TextField;
import javafx.scene.input.MouseEvent;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import javafx.stage.StageStyle;
import service.Hashmdp;
import service.User;

import java.io.IOException;
import java.net.URL;
import java.sql.SQLException;
import java.util.Optional;
import java.util.ResourceBundle;

import static service.Hashmdp.hashPassword;


public class ConnecxionController implements Initializable {

    @FXML
    private Button btnInscrire;

    @FXML
    private Button btnfermer;

    @FXML
    private TextField mdpConfField;
    @FXML
    private Text errormessage;
    @FXML
    private Text textenregistrement;

    @FXML
    private TextField mdpfield;

    @FXML
    private TextField nomfield;

    @FXML
    private TextField prenomfield;

    @FXML
    private TextField telephonefield;
    UserDB userdb = new UserDB();

    @FXML
    void closeWin(MouseEvent event) {
        Alert alert = new Alert(Alert.AlertType.ERROR);
        alert.setTitle("Fermeture");
        alert.setHeaderText("Fermeture de la fenêtre");
        alert.setContentText("Êtes-vous sûr de vouloir fermer cette fenêtre ?");

        Optional<ButtonType> result = alert.showAndWait();
        if (result.isPresent() && result.get() == ButtonType.OK) {
            // L'utilisateur a cliqué sur OK → on ferme la fenêtre
            Stage stage = (Stage) btnfermer.getScene().getWindow();
            stage.close(); // ferme la fenêtre

        }


    }

    @FXML
    void inscription(MouseEvent event) throws IOException, SQLException {
        // pour verifier si les tout les champs sont remplie
        if (nomfield.getText().isBlank() ||
                prenomfield.getText().isBlank() ||
                telephonefield.getText().isBlank() ||
                mdpfield.getText().isBlank() ||
                mdpConfField.getText().isBlank()) {
            Alert alert = new Alert(Alert.AlertType.ERROR);
            alert.setTitle("erreur");
            alert.setHeaderText("veuillez remplir toute les champs ");
            alert.setContentText("veuillez verifier les differents champs !  ?");

            alert.showAndWait();


        }
        else {
            //si tout les champ sont remplie
            String nom = nomfield.getText();
            String prenom = prenomfield.getText();
            String telephone = telephonefield.getText();
            String motdepasse = hashPassword(mdpfield.getText()) ;
            String mdpconfirmation = hashPassword(mdpConfField.getText());

            if (motdepasse.equals(mdpconfirmation)){
                // si les 2 mdp se valent
                Alert alert = new Alert(Alert.AlertType.CONFIRMATION);
                alert.setTitle("confirmation");
                alert.setHeaderText("veuillez confirmer votre enregistrment");
                alert.setContentText("   ");
                Optional<ButtonType> result = alert.showAndWait();

                    //si  user confirme sont inscription


                if (result.isPresent() && result.get() == ButtonType.OK) {

                    // L'utilisateur a cliqué sur OK → on ferme la fenêtre
                    User user = new User(nom,prenom,telephone,motdepasse);
                    boolean bool = userdb.createUser(user);
                    if (bool) {
                        System.out.println("great !"+user.getNom());
                        textenregistrement.setVisible(true);

                        Parent root = FXMLLoader.load(getClass().getResource("primary.fxml"));

                        Stage stage =(Stage) btnInscrire.getScene().getWindow();
                        stage.setScene(new Scene(root));
                        stage.setFullScreen(true);
                        stage.show();

                    }
                    // so a boyi
                    else{
                        errormessage.setVisible(true);
                        nomfield.clear();
                        prenomfield.clear();
                        telephonefield.clear();
                        mdpfield.clear() ;
                        mdpConfField.clear();

                    }

                }



                // si les 2 mdp sont different

            }
            else {
                Alert alert = new Alert(Alert.AlertType.ERROR);

                alert.setTitle("erreur");
                alert.setHeaderText("les mots de passe ne corespondent pas  ");
                alert.setContentText("veuillez verifier les mot de passe   ?");
                Optional<ButtonType> result = alert.showAndWait();

                if(result.isPresent() && result.get() == ButtonType.OK){

                }
            }

        }


    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        System.out.println(" ");
    }
}
