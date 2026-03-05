import platform
import os
import re
from pathlib import Path



os_name:str = platform.system()


def clear_screen() -> None:
    if os_name == "Windows":
        os.system('cls')
    else:
        os.system('clear')


# PROGRAMA PRINCIPAL

clear_screen()
java_project_name_pattern:str = r"^[a-zA-Z_$][a-zA-Z_$0-9]*$"
while(True):
    java_project_name:str = input("Digite o nome do projeto Java: ")
    if re.fullmatch(java_project_name_pattern, java_project_name):
        break
    else:
        clear_screen()
        print("Falha! Nome inválido ou não convencional para um projeto Java.")

clear_screen()
while(True):
    build_tool:str = input("1 | Vanilla \n2 | Maven \n3 | Gradle \n\n|| ")

    match build_tool:
        case '1':
            build_tool = "vanilla"
            break
        case '2':
            build_tool = "maven"
            break
        case '3':
            build_tool = "gradle"
            break
        
        case _:
                clear_screen()
                print("Opção inválida! Tente novamente.")

if build_tool != "vanilla":
    clear_screen()
    while(True):
        print("Gostaria de usar Spring Boot?")
        choose:str = input("1 | Sim \n2 | Não \n\n|| ")

        match choose:
            case '1':
                spring_boot:bool = True
                break
            case '2':
                spring_boot:bool = False
                break
            case _:
                    clear_screen()
                    print("Opção inválida! Tente novamente.")



# CRIANDO DIRETÓRIOS E ARQUIVOS

#diretório onde o script está sendo executado
base_dir = Path(__file__).resolve().parent

#criação de diretórios e subdiretórios
project_path = base_dir / java_project_name
project_path.mkdir(exist_ok=True)


if build_tool == "vanilla":
    src_path = project_path / "src" / "application"
    src_path.mkdir(parents=True, exist_ok=True)
else:
    src_path = project_path / "src" / "main" / "java" / "application"
    src_path.mkdir(parents=True, exist_ok=True)

file_ProgramJava:Path = src_path / "Program.java"
if(spring_boot):
    file_ProgramJava.write_text("""
    package application;

    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.context.ApplicationContext;
    import java.util.Arrays;

    @SpringBootApplication
    public class Program {

        public static void main(String[] args) {
            ApplicationContext ctx = SpringApplication.run(Program.class, args);

            System.out.println("--- Teste Spring Boot ---");
            System.out.println("Spring Boot está rodando!");

            int beanCount = ctx.getBeanDefinitionCount();
            System.out.println("Componentes (Beans) carregados: " + beanCount);
            
        }
    }
    """)
else:
    file_ProgramJava.write_text("""
    package application;

    public class Program {

        public static void main(String[] args) {
            // TODO Auto-generated method stub
            System.out.println("Hello, World");
        }

    }
    """)

#.gitignore
file_gitignore:Path = project_path / ".gitignore"
file_gitignore.write_text("""
# Created by https://www.toptal.com/developers/gitignore/api/java,maven,gradle,intellij,eclipse,visualstudiocode,netbeans
# Edit at https://www.toptal.com/developers/gitignore?templates=java,maven,gradle,intellij,eclipse,visualstudiocode,netbeans

### Eclipse ###
.metadata
bin/
tmp/
*.tmp
*.bak
*.swp
*~.nib
local.properties
.settings/
.loadpath
.recommenders

# External tool builders
.externalToolBuilders/

# Locally stored "Eclipse launch configurations"
*.launch

# PyDev specific (Python IDE for Eclipse)
*.pydevproject

# CDT-specific (C/C++ Development Tooling)
.cproject

# CDT- autotools
.autotools

# Java annotation processor (APT)
.factorypath

# PDT-specific (PHP Development Tools)
.buildpath

# sbteclipse plugin
.target

# Tern plugin
.tern-project

# TeXlipse plugin
.texlipse

# STS (Spring Tool Suite)
.springBeans

# Code Recommenders
.recommenders/

# Annotation Processing
.apt_generated/
.apt_generated_test/

# Scala IDE specific (Scala & Java development for Eclipse)
.cache-main
.scala_dependencies
.worksheet

# Uncomment this line if you wish to ignore the project description file.
# Typically, this file would be tracked if it contains build/dependency configurations:
#.project

### Eclipse Patch ###
# Spring Boot Tooling
.sts4-cache/

### Intellij ###
# Covers JetBrains IDEs: IntelliJ, RubyMine, PhpStorm, AppCode, PyCharm, CLion, Android Studio, WebStorm and Rider
# Reference: https://intellij-support.jetbrains.com/hc/en-us/articles/206544839

# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# Gradle and Maven with auto-import
# When using Gradle or Maven with auto-import, you should exclude module files,
# since they will be recreated, and may cause churn.  Uncomment if using
# auto-import.
# .idea/artifacts
# .idea/compiler.xml
# .idea/jarRepositories.xml
# .idea/modules.xml
# .idea/*.iml
# .idea/modules
# *.iml
# *.ipr

# CMake
cmake-build-*/

# Mongo Explorer plugin
.idea/**/mongoSettings.xml

# File-based project format
*.iws

# IntelliJ
out/

# mpeltonen/sbt-idea plugin
.idea_modules/

# JIRA plugin
atlassian-ide-plugin.xml

# Cursive Clojure plugin
.idea/replstate.xml

# SonarLint plugin
.idea/sonarlint/

# Crashlytics plugin (for Android Studio and IntelliJ)
com_crashlytics_export_strings.xml
crashlytics.properties
crashlytics-build.properties
fabric.properties

# Editor-based Rest Client
.idea/httpRequests

# Android studio 3.1+ serialized cache file
.idea/caches/build_file_checksums.ser

### Intellij Patch ###
# Comment Reason: https://github.com/joeblau/gitignore.io/issues/186#issuecomment-215987721

# *.iml
# modules.xml
# .idea/misc.xml
# *.ipr

# Sonarlint plugin
# https://plugins.jetbrains.com/plugin/7973-sonarlint
.idea/**/sonarlint/

# SonarQube Plugin
# https://plugins.jetbrains.com/plugin/7238-sonarqube-community-plugin
.idea/**/sonarIssues.xml

# Markdown Navigator plugin
# https://plugins.jetbrains.com/plugin/7896-markdown-navigator-enhanced
.idea/**/markdown-navigator.xml
.idea/**/markdown-navigator-enh.xml
.idea/**/markdown-navigator/

# Cache file creation bug
# See https://youtrack.jetbrains.com/issue/JBR-2257
.idea/$CACHE_FILE$

# CodeStream plugin
# https://plugins.jetbrains.com/plugin/12206-codestream
.idea/codestream.xml

# Azure Toolkit for IntelliJ plugin
# https://plugins.jetbrains.com/plugin/8053-azure-toolkit-for-intellij
.idea/**/azureSettings.xml

### Java ###
# Compiled class file
*.class

# Log file
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files #
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*
replay_pid*

### Maven ###
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup
pom.xml.next
release.properties
dependency-reduced-pom.xml
buildNumber.properties
.mvn/timing.properties
# https://github.com/takari/maven-wrapper#usage-without-binary-jar
.mvn/wrapper/maven-wrapper.jar

# Eclipse m2e generated files
# Eclipse Core
.project
# JDT-specific (Eclipse Java Development Tools)
.classpath

### NetBeans ###
**/nbproject/private/
**/nbproject/Makefile-*.mk
**/nbproject/Package-*.bash
build/
nbbuild/
dist/
nbdist/
.nb-gradle/

### VisualStudioCode ###
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
!.vscode/*.code-snippets

# Local History for Visual Studio Code
.history/

# Built Visual Studio Code Extensions
*.vsix

### VisualStudioCode Patch ###
# Ignore all local history of files
.history
.ionide

### Gradle ###
.gradle
**/build/
!src/**/build/

# Ignore Gradle GUI config
gradle-app.setting

# Avoid ignoring Gradle wrapper jar file (.jar files are usually ignored)
!gradle-wrapper.jar

# Avoid ignore Gradle wrappper properties
!gradle-wrapper.properties

# Cache of project
.gradletasknamecache

# Eclipse Gradle plugin generated files
# Eclipse Core
# JDT-specific (Eclipse Java Development Tools)

### Gradle Patch ###
# Java heap dump
*.hprof

# End of https://www.toptal.com/developers/gitignore/api/java,maven,gradle,intellij,eclipse,visualstudiocode,netbeans
""")

#.dockerignore
file_dockerignore:Path = project_path / ".dockerignore"
file_dockerignore.write_text("""
# Git
.git
.gitignore

# IDEs
.metadata
.idea
.vscode
.settings
nbproject
.project
.classpath
*.iml
*.iws

# Build output
target
build
out
nbbuild
dist
nbdist
.gradle

# Logs
*.log

# OS files
.DS_Store
Thumbs.db

# Temporary files
tmp
*.tmp
*.bak
*.swp
*~
.cache-main
.scala_dependencies
.worksheet
.history
.ionide

# Heap dump
*.hprof

# VSCode extensions
*.vsix

# Maven timing
.mvn/timing.properties
"""
)

#README.md
file_READMEmd:Path = project_path / "README.md"
file_READMEmd.write_text(f"""
# {java_project_name}

## Primeira execução / Rebuild
```
docker compose up --build
```

## Iniciar
```
docker compose up
```

## Encerrar
```
docker compose down
```
""")



if(build_tool == "maven"):
    parent_section = ""
    dependencies_section = ""

    if spring_boot:
        parent_section = """
<parent>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-parent</artifactId>
    <version>3.2.0</version>
</parent>
"""
        
        dependencies_section = """
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
    </dependency>
</dependencies>
"""
    #pom.xml
    file_pomXml: Path = project_path / "pom.xml"
    file_pomXml.write_text(f"""
<project xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>
    {parent_section}

    <groupId>com.example</groupId>
    <artifactId>{java_project_name}</artifactId>
    <version>1.0</version>

    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
    </properties>
    {dependencies_section}
</project>
""")
    

if(build_tool == "gradle"):
    file_settings: Path = project_path / "settings.gradle"
    file_settings.write_text(f"rootProject.name = '{java_project_name}'")

    # Valores padrão para Vanilla
    plugins_section = "id 'java'\n    id 'application'" 
    dependencies_section = "" # Fica vazio para Vanilla
    main_class_config = "application { mainClass = 'application.Program' }"
    
    if spring_boot:
        plugins_section = """
    id 'java'
    id 'org.springframework.boot' version '3.2.0'
    id 'io.spring.dependency-management' version '1.1.4'"""
        
        # AQUI ESTAVA O ERRO: Precisamos preencher as dependências!
        dependencies_section = """
dependencies {
    implementation 'org.springframework.boot:spring-boot-starter'
}"""
        main_class_config = "" # Spring não usa esse bloco

    file_build: Path = project_path / "build.gradle"
    file_build.write_text(f"""
plugins {{
    {plugins_section}
}}

group = 'com.example'
version = '1.0'
sourceCompatibility = '21'

repositories {{
    mavenCentral()
}}
{dependencies_section}
{main_class_config}
""")



if(build_tool == "vanilla"):
    docker_image = "eclipse-temurin:21-jdk-jammy"
    docker_command = "sh -c 'javac -d bin $(find src -name \"*.java\") && java -cp bin application.Program'"
    docker_copy = "COPY src ./src"

if(build_tool == "maven"):
    docker_image = "maven:3.9.6-eclipse-temurin-21"
    docker_command = "mvn -q compile exec:java -Dexec.mainClass='application.Program'"
    docker_copy = "COPY pom.xml .\nCOPY src ./src"

if(build_tool == "gradle"):
    docker_image = "gradle:8.6-jdk21"
    run_cmd = "bootRun" if spring_boot else "run"
    docker_command = f"gradle {run_cmd} -q --console=plain"
    docker_copy = "COPY build.gradle settings.gradle .\nCOPY src ./src"


#Dockerfile
file_Dockerfile: Path = project_path / "Dockerfile"
file_Dockerfile.write_text(f"""
FROM {docker_image}

WORKDIR /app

{docker_copy}

# No Maven/Gradle, o comando de execução geralmente compila antes
# No Vanilla, precisamos do mkdir bin (que já está no seu comando de execução)
CMD [{docker_command}]
""")

#docker-compose.yml
file_dockerComposeYml: Path = project_path / "docker-compose.yml"
file_dockerComposeYml.write_text(f"""
services:
    {java_project_name}:
        build: .
        volumes:
            - .:/app
        stdin_open: true
        tty: true
        command: {docker_command}
""")