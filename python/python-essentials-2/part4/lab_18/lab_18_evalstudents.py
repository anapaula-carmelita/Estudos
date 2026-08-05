class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    pass


def evalstudents():
    stream = None
    try:
        filename = input("Enter the filename: ")
        stream = open(filename, "rt", encoding = "utf-8")
        scores = {}
        students = []
        while 1:
            line = stream.readline()

            if line == '':
                if len(scores) == 0:
                    raise FileEmpty
                break
            
            student = line.split()
            
            if len(student) != 3:
                raise BadLine
            
            name = student[0] + ' ' + student[1]

            try:
                score = float(student[2])
            except ValueError:
                raise BadLine
            

            # Pega o score atual (ou 0 se não existir) e soma com o novo
            scores[name] = scores.get(name, 0) + score
        
        for s in sorted(scores.keys()):
            print(f'{s}\t{scores[s]}')

    except FileNotFoundError as e:
        print('FileNotFoundError:', e.args)
    except FileEmpty:
        print('FileEmpty: File is empty')
    except BadLine:
        print('BadLine: Line is bad, missing something or corrupted data')
    except BaseException as e: # Boa prática para capturar qualquer outro erro imprevisto
        print('Error:', e.args)
    finally:
        if stream is not None:
            stream.close()

if __name__ == '__main__':
    evalstudents()

        
