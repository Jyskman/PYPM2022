// Python includes
#include <python3.9/Python.h>
//
// STD includes
#include <stdio.h>
#include "test.h"
#include "PY_PM.h"

#include "numpy/ndarraytypes.h"
#include "numpy/arrayobject.h"
#include "numpy/ufuncobject.h"
#include "numpy/npy_3kcompat.h"

#include <string>
#include <cstring>


 // sudo python3 setup.py install

//-----------------------------------------------------------------------------


//~ class test {
	//~ public:
	//~ int a = 1;
	//~ int b = 1;
	//~ int c = 0;
	//~ test();
	//~ void method_1();
//~ };

//~ test::test() {};

//~ void test::method_1() {
  
  //~ c = a + b;
  
  
//~ };


void test_destroy(PyObject *tester) {
  
    delete (test*)PyCapsule_GetPointer(tester,"testptr");
  
};

static PyObject *test_example(PyObject *self, PyObject *args) {
  
    std::string s = "hej";
    std::string ss = "hejs";

    PyObject * ret = Py_BuildValue("[s,s]",s.c_str(),ss.c_str());
        
    return ret;
};

static PyObject *test_method2(PyObject *self, PyObject *args) {
  
    PyObject * pf = NULL;
        
    if(!PyArg_UnpackTuple(args, "funk", 1, 1, &pf)) return NULL;
    //~ test * test_object = reinterpret_cast<test>(PyCapsule_GetPointer(testCapsule, "testptr"));
    test * local = (test*)PyCapsule_GetPointer(pf, "testptr") ;
    //~ testCapsule->method_1();
    local->method_2();
    PySys_WriteStdout("c is, %d! :)\n", local->c);

    return pf;
};

static PyObject *hello_example(PyObject *self, PyObject *args)
{
  // Unpack a string from the arguments
  const char *strArg;
  if (!PyArg_ParseTuple(args, "s", &strArg))
    return NULL;

  // Print message and return None
  PySys_WriteStdout("Hello Jyskk-yu, %s! :)\n", strArg);
  Py_RETURN_NONE;
}

// OPC objects ------

void OPC_destroy(PyObject *tester) {
  
    delete (OPC*)PyCapsule_GetPointer(tester,"opcptr");
  
};

static PyObject *OPC_create(PyObject *self, PyObject *args) {
  
    OPC * OPC_object = new OPC;
    
    PyObject *OPC_Capsule = PyCapsule_New( (void *)OPC_object,  "opcptr",OPC_destroy );
    
    return OPC_Capsule;
};


static PyObject *ISS_config(PyObject *self, PyObject *args) {
  
    PyObject * pf = NULL;
        
    if(!PyArg_UnpackTuple(args, "iss", 1, 1, &pf)) return NULL;

    OPC * local = (OPC*)PyCapsule_GetPointer(pf, "opcptr") ;

    local->ISS_setup();
    
    //~ delete local;
    
    Py_RETURN_NONE;

    

};

static PyObject *OPC_close(PyObject *self, PyObject *args) {
  
    PyObject * pf = NULL;
        
    if(!PyArg_UnpackTuple(args, "iss", 1, 1, &pf)) return NULL;

    OPC * local = (OPC*)PyCapsule_GetPointer(pf, "opcptr") ;

    local->OPC_close();
    
    //~ delete local;
    
    Py_RETURN_NONE;
    

};

static PyObject *OPC_fan_off(PyObject *self, PyObject *args) {
  
    PyObject * pf = NULL;
        
    if(!PyArg_UnpackTuple(args, "iss", 1, 1, &pf)) return NULL;

    OPC * local = (OPC*)PyCapsule_GetPointer(pf, "opcptr") ;

    local->OPC_fan(false);
    
    //~ delete local;
    
    Py_RETURN_NONE;
    

};

static PyObject *OPC_fan_on(PyObject *self, PyObject *args) {
  
    PyObject * pf = NULL;
        
    if(!PyArg_UnpackTuple(args, "iss", 1, 1, &pf)) return NULL;

    OPC * local = (OPC*)PyCapsule_GetPointer(pf, "opcptr") ;

    local->OPC_fan(true);
    
    //~ delete local;
    
    Py_RETURN_NONE;
    

};

static PyObject *OPC_return_ch(PyObject *self, PyObject *args) {
  
    PyObject * pf = NULL;
        
    if(!PyArg_UnpackTuple(args, "iss", 1, 1, &pf)) return NULL;

    OPC * local = (OPC*)PyCapsule_GetPointer(pf, "opcptr") ;

    local->OPC_read_config();
    
    int bin[25];
    
    
    
    bin[0] = local->OPC_struct_config_variables.binBoundriesDiametor0;
    bin[1] = local->OPC_struct_config_variables.binBoundriesDiametor1;
    bin[2] = local->OPC_struct_config_variables.binBoundriesDiametor2;
    bin[3] = local->OPC_struct_config_variables.binBoundriesDiametor3;
    bin[4] = local->OPC_struct_config_variables.binBoundriesDiametor4;
    bin[5] = local->OPC_struct_config_variables.binBoundriesDiametor5;
    bin[6] = local->OPC_struct_config_variables.binBoundriesDiametor6;
    bin[7] = local->OPC_struct_config_variables.binBoundriesDiametor7;
    bin[8] = local->OPC_struct_config_variables.binBoundriesDiametor8;
    bin[9] = local->OPC_struct_config_variables.binBoundriesDiametor9;
    bin[10] = local->OPC_struct_config_variables.binBoundriesDiametor10;
    bin[11] = local->OPC_struct_config_variables.binBoundriesDiametor11;
    bin[12] = local->OPC_struct_config_variables.binBoundriesDiametor12;
    bin[13] = local->OPC_struct_config_variables.binBoundriesDiametor13;
    bin[14] = local->OPC_struct_config_variables.binBoundriesDiametor14;
    bin[15] = local->OPC_struct_config_variables.binBoundriesDiametor15;
    bin[16] = local->OPC_struct_config_variables.binBoundriesDiametor16;
    bin[17] = local->OPC_struct_config_variables.binBoundriesDiametor17;
    bin[18] = local->OPC_struct_config_variables.binBoundriesDiametor18;
    bin[19] = local->OPC_struct_config_variables.binBoundriesDiametor19;
    bin[20] = local->OPC_struct_config_variables.binBoundriesDiametor20;
    bin[21] = local->OPC_struct_config_variables.binBoundriesDiametor21;
    bin[22] = local->OPC_struct_config_variables.binBoundriesDiametor22;
    bin[23] = local->OPC_struct_config_variables.binBoundriesDiametor23;
    bin[24] = local->OPC_struct_config_variables.binBoundriesDiametor24;
    
    
    
    //~ OPC_Configuration_Variables
    
    for ( int i = 0; i < 25; i++ ) {
    
     PySys_WriteStdout("Hello Jysk, %d! :)\n", bin[i]);
    };
    
   
    npy_intp dims[1];
    npy_intp a = 25;
    dims[0] = a;


    //~ PyObject * ret = PyArray_SimpleNewFromData(1,dims,NPY_FLOAT,arr);
    //~ PyObject * ret = PyArray_SimpleNewFromData(1,dims,NPY_INT32,&arr_e);
    PyObject * ret = PyArray_Zeros(1,dims,PyArray_DescrFromType(NPY_INT),0);

    for ( int i = 0; i < 25; i++ ) {

        npy_intp ad = i; // position for returened pointer
        int * data = (int*)PyArray_GetPtr((PyArrayObject*)ret,&ad);
        *data = bin[i];
    };
    
    
    
    //~ delete local;
    
    return ret;
    

};

static PyObject *OPC_return_counts(PyObject *self, PyObject *args) {
  
    PyObject * pf = NULL;
        
    if(!PyArg_UnpackTuple(args, "iss", 1, 1, &pf)) return NULL;

    OPC * local = (OPC*)PyCapsule_GetPointer(pf, "opcptr") ;

    local->OPC_read_histogram();
    
    int bin[24];
    
    
    
    bin[0] = local->OPC_struct_histogram.binCount0;
    bin[1] = local->OPC_struct_histogram.binCount1;
    bin[2] = local->OPC_struct_histogram.binCount2;
    bin[3] = local->OPC_struct_histogram.binCount3;
    bin[4] = local->OPC_struct_histogram.binCount4;
    bin[5] = local->OPC_struct_histogram.binCount5;
    bin[6] = local->OPC_struct_histogram.binCount6;
    bin[7] = local->OPC_struct_histogram.binCount7;
    bin[8] = local->OPC_struct_histogram.binCount8;
    bin[9] = local->OPC_struct_histogram.binCount9;
    bin[10] = local->OPC_struct_histogram.binCount10;
    bin[11] = local->OPC_struct_histogram.binCount11;
    bin[12] = local->OPC_struct_histogram.binCount12;
    bin[13] = local->OPC_struct_histogram.binCount13;
    bin[14] = local->OPC_struct_histogram.binCount14;
    bin[15] = local->OPC_struct_histogram.binCount15;
    bin[16] = local->OPC_struct_histogram.binCount16;
    bin[17] = local->OPC_struct_histogram.binCount17;
    bin[18] = local->OPC_struct_histogram.binCount18;
    bin[19] = local->OPC_struct_histogram.binCount19;
    bin[20] = local->OPC_struct_histogram.binCount20;
    bin[21] = local->OPC_struct_histogram.binCount21;
    bin[22] = local->OPC_struct_histogram.binCount22;
    bin[23] = local->OPC_struct_histogram.binCount23;

    
    //~ OPC_Configuration_Variables
    
    //~ for ( int i = 0; i < 25; i++ ) {
    
     //~ PySys_WriteStdout("Hello Jysk, %d! :)\n", bin[i]);
    //~ };
    
   
    npy_intp dims[1];
    npy_intp a = 24;
    dims[0] = a;


    //~ PyObject * ret = PyArray_SimpleNewFromData(1,dims,NPY_FLOAT,arr);
    //~ PyObject * ret = PyArray_SimpleNewFromData(1,dims,NPY_INT32,&arr_e);
    PyObject * ret = PyArray_Zeros(1,dims,PyArray_DescrFromType(NPY_INT),0);

    for ( int i = 0; i < 24; i++ ) {

        npy_intp ad = i; // position for returened pointer
        int * data = (int*)PyArray_GetPtr((PyArrayObject*)ret,&ad);
        *data = bin[i];
    };
    
    
    
    //~ delete local;
    
    return ret;
    

};

static PyObject *OPC_return_dist(PyObject *self, PyObject *args) {
  
    PyObject * pf = NULL;
        
    if(!PyArg_UnpackTuple(args, "iss", 1, 1, &pf)) return NULL;

    OPC * local = (OPC*)PyCapsule_GetPointer(pf, "opcptr") ;

    local->OPC_read_histogram();
    
    float bin[24];
    
    
    
    bin[0] = (float)local->OPC_struct_histogram.binCount0;
    bin[1] = (float)local->OPC_struct_histogram.binCount1;
    bin[2] = (float)local->OPC_struct_histogram.binCount2;
    bin[3] = (float)local->OPC_struct_histogram.binCount3;
    bin[4] = (float)local->OPC_struct_histogram.binCount4;
    bin[5] = (float)local->OPC_struct_histogram.binCount5;
    bin[6] = (float)local->OPC_struct_histogram.binCount6;
    bin[7] = (float)local->OPC_struct_histogram.binCount7;
    bin[8] = (float)local->OPC_struct_histogram.binCount8;
    bin[9] = (float)local->OPC_struct_histogram.binCount9;
    bin[10] = (float)local->OPC_struct_histogram.binCount10;
    bin[11] = (float)local->OPC_struct_histogram.binCount11;
    bin[12] = (float)local->OPC_struct_histogram.binCount12;
    bin[13] = (float)local->OPC_struct_histogram.binCount13;
    bin[14] = (float)local->OPC_struct_histogram.binCount14;
    bin[15] = (float)local->OPC_struct_histogram.binCount15;
    bin[16] = (float)local->OPC_struct_histogram.binCount16;
    bin[17] = (float)local->OPC_struct_histogram.binCount17;
    bin[18] = (float)local->OPC_struct_histogram.binCount18;
    bin[19] = (float)local->OPC_struct_histogram.binCount19;
    bin[20] = (float)local->OPC_struct_histogram.binCount20;
    bin[21] = (float)local->OPC_struct_histogram.binCount21;
    bin[22] = (float)local->OPC_struct_histogram.binCount22;
    bin[23] = (float)local->OPC_struct_histogram.binCount23;

    
    //~ OPC_Configuration_Variables
    
    float ml = ( (float)local->OPC_struct_histogram.samplingPeriod * (float)local->OPC_struct_histogram.sampleFlowRate)/10000.0 ;
   
   
    //PySys_WriteStdout("ml, %f! :)\n", ml);
    //PySys_WriteStdout("sampling period int , %d! :)\n", local->OPC_struct_histogram.samplingPeriod/100);
    //PySys_WriteStdout("sampling flow rate int , %d! :)\n", local->OPC_struct_histogram.sampleFlowRate/100);
    //PySys_WriteStdout("sampling period float , %f! :)\n", (float)local->OPC_struct_histogram.samplingPeriod/100.0);
    //PySys_WriteStdout("sampling flow rate float , %f! :)\n", (float)local->OPC_struct_histogram.sampleFlowRate/100.0);
   
   
    for ( int i = 0; i < 24; i++ ) {
    
        bin[i] = bin[i] / (float)ml;
    
        //~ PySys_WriteStdout("Hello Jysk, %f! :)\n", ml);
        
     
     
     
    };
    
   
    npy_intp dims[1];
    npy_intp a = 24;
    dims[0] = a;


    //~ PyObject * ret = PyArray_SimpleNewFromData(1,dims,NPY_FLOAT,arr);
    //~ PyObject * ret = PyArray_SimpleNewFromData(1,dims,NPY_INT32,&arr_e);
    PyObject * ret = PyArray_Zeros(1,dims,PyArray_DescrFromType(NPY_FLOAT),0);

    for ( int i = 0; i < 24; i++ ) {

        npy_intp ad = i; // position for returened pointer
        float * data = (float*)PyArray_GetPtr((PyArrayObject*)ret,&ad);
        *data = bin[i];
    };
    
    
    
    //~ delete local;
    
    return ret;
    

};

static PyObject *pickup(PyObject *self, PyObject *args) {
    

    PySys_WriteStdout("2022 test");
    
    Py_RETURN_NONE;
};



// read configuration variables
static PyObject *OPC_return_bounds(PyObject *self, PyObject *args) {
  
    PyObject * pf = NULL;
        
    if(!PyArg_UnpackTuple(args, "iss", 1, 1, &pf)) return NULL;

    OPC * local = (OPC*)PyCapsule_GetPointer(pf, "opcptr") ;


    local->OPC_read_config();


    //int bin_bounds[50];

    
    //bin_bounds[0] = (float)local->OPC_struct_config_variables.binBoundriesADC0;
    //bin_bounds[1] = (float)local->OPC_struct_config_variables.binBoundriesADC1;
    //bin_bounds[2] = (float)local->OPC_struct_config_variables.binBoundriesADC2;
    //bin_bounds[3] = (float)local->OPC_struct_config_variables.binBoundriesADC3;
    //bin_bounds[4] = (float)local->OPC_struct_config_variables.binBoundriesADC4;
    //bin_bounds[5] = (float)local->OPC_struct_config_variables.binBoundriesADC5;
    //bin_bounds[6] = (float)local->OPC_struct_config_variables.binBoundriesADC6;
    //bin_bounds[7] = (float)local->OPC_struct_config_variables.binBoundriesADC7;
    //bin_bounds[8] = (float)local->OPC_struct_config_variables.binBoundriesADC8;
    //bin_bounds[9] = (float)local->OPC_struct_config_variables.binBoundriesADC9;
    //bin_bounds[10] = (float)local->OPC_struct_config_variables.binBoundriesADC10;
    //bin_bounds[11] = (float)local->OPC_struct_config_variables.binBoundriesADC11;
    //bin_bounds[12] = (float)local->OPC_struct_config_variables.binBoundriesADC12;
    //bin_bounds[13] = (float)local->OPC_struct_config_variables.binBoundriesADC13;
    //bin_bounds[14] = (float)local->OPC_struct_config_variables.binBoundriesADC14;
    //bin_bounds[15] = (float)local->OPC_struct_config_variables.binBoundriesADC15;
    //bin_bounds[16] = (float)local->OPC_struct_config_variables.binBoundriesADC16;
    //bin_bounds[17] = (float)local->OPC_struct_config_variables.binBoundriesADC17;
    //bin_bounds[18] = (float)local->OPC_struct_config_variables.binBoundriesADC18;
    //bin_bounds[19] = (float)local->OPC_struct_config_variables.binBoundriesADC19;
    //bin_bounds[20] = (float)local->OPC_struct_config_variables.binBoundriesADC20;
    //bin_bounds[21] = (float)local->OPC_struct_config_variables.binBoundriesADC21;
    //bin_bounds[22] = (float)local->OPC_struct_config_variables.binBoundriesADC22;
    //bin_bounds[23] = (float)local->OPC_struct_config_variables.binBoundriesADC23;
    //bin_bounds[24] = (float)local->OPC_struct_config_variables.binBoundriesADC24;    

//// Part 2

    //bin_bounds[25] = (float)local->OPC_struct_config_variables.binBoundriesDiametor0;
    //bin_bounds[26] = (float)local->OPC_struct_config_variables.binBoundriesDiametor1;
    //bin_bounds[27] = (float)local->OPC_struct_config_variables.binBoundriesDiametor2;
    //bin_bounds[28] = (float)local->OPC_struct_config_variables.binBoundriesDiametor3;
    //bin_bounds[29] = (float)local->OPC_struct_config_variables.binBoundriesDiametor4;
    //bin_bounds[30] = (float)local->OPC_struct_config_variables.binBoundriesDiametor5;
    //bin_bounds[31] = (float)local->OPC_struct_config_variables.binBoundriesDiametor6;
    //bin_bounds[32] = (float)local->OPC_struct_config_variables.binBoundriesDiametor7;
    //bin_bounds[33] = (float)local->OPC_struct_config_variables.binBoundriesDiametor8;
    //bin_bounds[34] = (float)local->OPC_struct_config_variables.binBoundriesDiametor9;
    //bin_bounds[35] = (float)local->OPC_struct_config_variables.binBoundriesDiametor10;
    //bin_bounds[36] = (float)local->OPC_struct_config_variables.binBoundriesDiametor11;
    //bin_bounds[37] = (float)local->OPC_struct_config_variables.binBoundriesDiametor12;
    //bin_bounds[38] = (float)local->OPC_struct_config_variables.binBoundriesDiametor13;
    //bin_bounds[39] = (float)local->OPC_struct_config_variables.binBoundriesDiametor14;
    //bin_bounds[40] = (float)local->OPC_struct_config_variables.binBoundriesDiametor15;
    //bin_bounds[41] = (float)local->OPC_struct_config_variables.binBoundriesDiametor16;
    //bin_bounds[42] = (float)local->OPC_struct_config_variables.binBoundriesDiametor17;
    //bin_bounds[43] = (float)local->OPC_struct_config_variables.binBoundriesDiametor18;
    //bin_bounds[44] = (float)local->OPC_struct_config_variables.binBoundriesDiametor19;
    //bin_bounds[45] = (float)local->OPC_struct_config_variables.binBoundriesDiametor20;
    //bin_bounds[46] = (float)local->OPC_struct_config_variables.binBoundriesDiametor21;
    //bin_bounds[47] = (float)local->OPC_struct_config_variables.binBoundriesDiametor22;
    //bin_bounds[48] = (float)local->OPC_struct_config_variables.binBoundriesDiametor23;
    //bin_bounds[49] = (float)local->OPC_struct_config_variables.binBoundriesDiametor24;  


    //return ret;
    
    Py_RETURN_NONE;
};

//-----------------------------------------------------------------------------
//~ static PyObject *elevation_example(PyObject *self, PyObject *args)
//~ {
  //~ // Return an integer
  //~ return PyLong_FromLong(21463L);
//~ }

//-----------------------------------------------------------------------------
static PyMethodDef pypm_methods[] = {
  {
    "hello",
    hello_example,
    METH_VARARGS,
    "Prints back 'Hello <param>', for example example: hello.hello('you')"
  },

  {
    "test",
    test_example,
    METH_VARARGS,
    "Returns elevation of Nevado Sajama."
  },
  {
    "test_method_2",
    test_method2,
    METH_VARARGS,
    "Returns elevation of Nevado Sajama."
  },
  {
    "OPC_create",
    OPC_create,
    METH_VARARGS,
    "Returns elevation of Nevado Sajama."
  },
  {
    "ISS_config",
    ISS_config,
    METH_VARARGS,
    "ISS"
  },
  {
    "OPC_close",
    OPC_close,
    METH_VARARGS,
    "ISS"
  },
  {
    "OPC_fan_off",
    OPC_fan_off,
    METH_VARARGS,
    "ISS"
  },
  {
    "OPC_fan_on",
    OPC_fan_on,
    METH_VARARGS,
    "ISS"
  },
    {
    "OPC_return_ch",
    OPC_return_ch,
    METH_VARARGS,
    "ISS"
  },
  {
    "OPC_return_counts",
    OPC_return_counts,
    METH_VARARGS,
    "ISS"
  },
    {
    "OPC_return_dist",
    OPC_return_dist,
    METH_VARARGS,
    "ISS"
  },
  
    {
    "pickup",
    pickup,
    METH_VARARGS,
    "ISS"
  },
 
    {
    "OPC_return_bounds",
    OPC_return_bounds,
    METH_VARARGS,
    "ISS"
  },  
  
  {NULL, NULL, 0, NULL}        /* Sentinel */
};

//-----------------------------------------------------------------------------
#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC init_hello(void)
{
  (void) Py_InitModule("_pypm2", pypm_methods);
}
#else /* PY_MAJOR_VERSION >= 3 */
static struct PyModuleDef pypm_module_def = {
  PyModuleDef_HEAD_INIT,
  "_pypm2",
  "Internal \"_pypm2\" module",
  -1,
  pypm_methods
};

PyMODINIT_FUNC PyInit__pypm2(void)
{
  import_array();
  return PyModule_Create(&pypm_module_def);
}
#endif /* PY_MAJOR_VERSION >= 3 */


//PYBIND11_MODULE( PY_PM, m ) {
	////~ m.doc() = "OPC N3 module for RPI using USB ISS";
	////~ m.def("add", &add, "Func");
	
	//py::class_<OPC>(m, "OPC")
	//.def(py::init())
	//.def("ISS_setup",&OPC::ISS_setup)
	//.def("OPC_close",&OPC::OPC_close)
	//.def("OPC_read_config",&OPC::OPC_read_config)
	//.def("OPC_fan",&OPC::OPC_fan)
	//.def("OPC_test_array",&OPC::test_array)
	//.def("OPC_read_histogram",&OPC::OPC_read_histogram);
	
	
//};
