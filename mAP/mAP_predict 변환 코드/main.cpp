#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <cstdlib>
#include <vector>

using namespace std;



int main()
{

    system("exec rm -r /home/tkol/mAP/predicted/*");


    string dist = "/home/tkol/mAP/valid_result/comp4_det_test_";
    vector<string> filePath;
    vector<string> label_name;

    ifstream label_Name_cfg("/home/tkol/darknet/mmi9/MyObj.names");



    string Path;
    string name;
    while(getline(label_Name_cfg, name)) {

        Path = dist + name + ".txt";
        filePath.push_back(Path);


        label_name.push_back(name);
    }





    // read File
    for(int i=0; i<filePath.size(); i++){
        ifstream openFile(filePath.at(i).data());

        if( openFile.is_open() ){

            string line;


            while(getline(openFile, line)){

                string frame_num;

                int location = line.find(" ");
                frame_num.append(line, 0, location);
                line.erase(0, location);                          
                line = label_name[i] + line;

                string outfilePath = "/home/tkol/mAP/predicted/" + frame_num + ".txt";

                ofstream outfile(outfilePath.c_str(), ios::app);
                outfile << line << endl;


                cout << line << '\n';

            }

            openFile.close();

        }

    }


    return 0;
}

