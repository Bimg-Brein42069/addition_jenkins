pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Bimg-Brein42069/addition_jenkins'
            }
        }
        stage('Provide permissions') {
            steps {
                sh "chmod u+x Prog1.py"
                sh "chmod u+x Test1.py"
                sh "chmod u+x Test2.py"
                sh "chmod u+x Test3.py"
                sh "chmod u+x Test4.py"
                sh "chmod u+x Test5.py"
            }
        }
        stage('Build Code'){
            steps{
                sh "./Prog1.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "./Test.py"
            }
        }
    } 
}
