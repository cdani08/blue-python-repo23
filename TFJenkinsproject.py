terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.10.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_key_pair" "my_key_pair" {
  key_name   = "my-ec2-key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQD8F36p0oCaoc5sHeB/IXaMEZvF/Rk2/VG8Lk9+/6JFPXiUguq+etC5GARyydyG5QjgBGreT1e4Th8fys+JR3PHnoU2c9J1K5l8+REbkfUppdch317AEPYO5lQdo9UHhH8HSpsSCbqN+rDRzcU/4aLBbr7BtWGEEPzllAIZsfdFika2nEPaVOCgJzBD0IkliTf+Sv4itwROZavZFVP7qBrfjbVHP5CvU7a8yNmvmBROPc3D8r5qACP4ia6obmO/ttvXjjO8Y2iKsLfr2gprtXSdUTnTtMHavSBsyPDlB2CcnCBvVZOguuVS8wV1iU9sqn1cEMWHg71a1WsMmBmRyZuYcUl6sCKD/maiKH6WTzbYnOb2hHhiFsbYvdquOZ6i0PcXny5AoJOHRhHBJToBtQ7tmJAra8xLhii9ANvXD0Vo8qGshatJrKWmoVyi5H4JKBPOIjIw8mvcMoGBuQqNMKE2zH0+X3K1u//lKYCzaD9tx2omVhWzDo7JTPgTSgRWTXmfowGcMF3GVW7qmlpnxP2+RTOliB3WkeUKgNufOma3NbT88nEGLYJO2oo9uYUQ4AkvxoYKBzeUMJDcQzHrFaHB8PuIY3KbIrW/rkYdL3LzMC2+cnThWXdg0tY6y5UXg0QenNcRiIUc0eRspcTv87v/i9rUcgCmmPmZonghR6mcDw== acjenk18@gmail.com"
}


resource "aws_instance" "MyWk20Project" {
  ami           = "ami-08a52ddb321b32a8c"
  instance_type = "t2.micro"
  security_groups = ["jenkins-sg20"]
  key_name              = aws_key_pair.my_key_pair.key_name

  tags = {
    Name = "mywk20project"
  }

  user_data = <<-EOF
  #!/bin/bash
  sudo yum update
  sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat/jenkins.repo
  sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
  sudo yum upgrade
  amazon-linux-extras install epel -y
  sudo dnf install java-11-amazon-corretto -y
  sudo yum install jenkins -y
  sudo systemctl enable jenkins
  sudo systemctl start jenkins
  EOF


}


resource "aws_security_group" "my-new-security_group" {
  name        = "jenkins-sg20"
  description = "Allow inbound traffic on tcp/22, tcp/8080"
  vpc_id      = "vpc-08dcd3e401fd54c83"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


resource "aws_s3_bucket" "bucket" {
  bucket = "cj23-wk-20-bucket"

  tags = {
    Name = "cj23-wk-20-bucket"
  }
}
