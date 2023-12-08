#define PY_SSIZE_T_CLEAN
#include <python3.11/pytypedefs.h>
#include <python3.11/Python.h>
#include <python3.11/pybuffer.h>
#include <python3.11/listobject.h>
#include <python3.11/floatobject.h>

static PyObject *foreign_matrix_power(PyObject *self, PyObject *args) {
    PyObject *buf;
    int columns;
    int pow;
    if (!PyArg_ParseTuple(args, "Oi", &buf, &pow)) {
        return NULL;
    }
    Py_INCREF(buf);
    int rows = PyList_Size(buf);
    float **matrix = malloc(sizeof(float*) * rows);
    PyObject **list = malloc(sizeof(PyObject*) * rows);
    for(int i = 0; i < rows; i++) {
        PyObject *row = PyList_GetItem(buf, i);
        columns = (int)PyList_Size(row);
        matrix[i] = malloc(sizeof(float) * columns);
        for (int j = 0; j < columns; j++) {
            float x  = PyFloat_AsDouble(PyList_GetItem(row, j));
            matrix[i][j] = x;
        }
    }
    float **result = malloc(sizeof(float*) * rows);
    for (size_t i = 0; i < rows; i++) {
        result[i] = calloc(columns, sizeof(float));
        for (size_t j = 0; j < rows; j++) {
            result[i][j] = matrix[i][j];
        }
        
    }
    for (size_t p = 0; p < pow - 1; p++) {
        for (size_t i = 0; i < rows; i++) {
            float *tmp = malloc(sizeof(float) * rows);
            for (size_t j = 0; j < columns; j++) {
                float s = 0;
                for (size_t k = 0; k < columns; k++) {
                    s += (result[i][k] * matrix[k][j]);
                }
                tmp[j] = s;
            }
            for (size_t j = 0; j < columns; j++) {
                result[i][j] = tmp[j];
            }
            free(tmp);
        }
    }
    for (size_t i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
    for (size_t i = 0; i < rows; i++) {
        PyObject* row = PyList_GetItem(buf, i);
        Py_INCREF(row);

        for (size_t j = 0; j < rows; j++) {
            PyList_SetItem(row, j, PyFloat_FromDouble(result[i][j]));
        }
        Py_DECREF(row);
    }
    for (size_t i = 0; i < rows; i++) {
        free(result[i]);
    }
    free(result);
    return buf;
}
static PyMethodDef ForeignMethods[] = {
    {
        "foreign_matrix_power",
        foreign_matrix_power, METH_VARARGS,
        "Bla bla bla",
    },
    {NULL, NULL, 0, NULL}
};
static struct PyModuleDef foreignmodule = {
    PyModuleDef_HEAD_INIT,
    "foreign", /* name of module */
    NULL, /* module documentation, may be NULL */
    -1, /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    ForeignMethods
};
PyMODINIT_FUNC PyInit_foreign(void) {
    return PyModule_Create(&foreignmodule);
}
