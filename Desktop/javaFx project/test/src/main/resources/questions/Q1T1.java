//package question;
//
//
//import editor.CodeEditor;
//
//import java.io.*;
//
//public class Q1T1 {
//
//
//    static String Question =" x= 10 , y= 5 alors output = 13\nx =30 , y=16 output = 44";
//
//    public static String getQuestion() {
//        return Question;
//    }
//
//    public static void initializeeditor(CodeEditor editor){
//        editor.replaceText("x=int(input()) \n" +
//                "y=int(input())\n\n\n\n" +
//                "// placer votre code ici\n\n\n\n\n\n" +
//                "print()#la sortie de votre code\n   ");
//
//
//    }
//
//    public static Boolean testQ(Process process) throws IOException {
//        Boolean etat = null;
//
//
//        BufferedWriter bfwriter = new BufferedWriter
//                (new OutputStreamWriter(process.getOutputStream()));
//
//        bfwriter.write("10\n");
//        bfwriter.write("13\n");
//
//        bfwriter.flush();
//        bfwriter.close();
//
//        BufferedReader output = new BufferedReader(
//                new InputStreamReader(process.getInputStream())
//        );
//
//        BufferedReader error = new BufferedReader(
//                new InputStreamReader(process.getErrorStream())
//        );
//        String expected = "21";
//
//        String line;
//        while ((line = output.readLine()) != null) {
//
//            if (line.equals(expected)) {
//                System.out.println("Bonne réponse");
//                etat = true;
//
//            } else {
//                System.out.println("Mauvaise réponse");
//                etat = false;
//
//            }
//
//        }
//
//        String er;
//        while ((er = error.readLine()) != null){
//            System.out.println(er);
//        }
//
//        return etat ;
//
//    }
//}
