pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git clone 'https://github.com/Bimg-Brein42069/addition_jenkins'
                cd addition_jenkins
            }
        }
        stage('Provide permissions') {
            steps {
                sh "chmod u+x Prog1.py"
                sh "chmod u+x Test.py"
            }
        }
        stage('Build Code'){
            steps{
                sh "./Prog1.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "./Test1.py"
                sh "./Test2.py"
                sh "./Test3.py"
                sh "./Test4.py"
                sh "./Test5.py"
            }
        }
    } 
}
