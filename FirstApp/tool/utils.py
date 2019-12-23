import os


def fileListFunc(filePathList):
    fileList = []
    for top, dirs, nondirs in os.walk(filePathList):
        for item in nondirs:
            fileList.append(os.path.join(top, item))
    return fileList


if __name__ == '__main__':
    path = r'E:\google drive'
    arr = fileListFunc(path)
    for a in range(len(arr)):
        print(arr[a])

