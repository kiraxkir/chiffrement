package service;



public class User {

    String nom;
    String prenom;
    String telephone;
    String mdp ;
    int id;


    public User(String nom, String prenon, String telephone, String mdp) {
        this.nom = nom;
        this.prenom = prenon;
        this.telephone = telephone;
        this.mdp = mdp;
    }


    public User(String nom, String prenom, String telephone, String mdp, int id) {
        this.nom = nom;
        this.prenom = prenom;
        this.telephone = telephone;

        this.mdp = mdp;
        this.id = id;
    }



    //getter

    public String getMdp() {
        return mdp;
    }

    public int getId() {
        return id;
    }

    public String getTelephone() {
        return telephone;
    }

    public String getPrenom() {
        return prenom;
    }

    public String getNom() {
        return nom;
    }
    // getter

    public void setId(int id) {
        this.id = id;
    }
}