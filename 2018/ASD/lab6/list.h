#ifndef LIST_H_
#define LIST_H_

    typedef struct task{
        char name[10]; // имя запроса
        unsigned time; // время обслуживания
        char type; //t1 - 1 t2 - 2 t3 - 3
    }base_type;

    extern const char list_ok;
    extern const char list_mem_error;
    extern const char list_over;
    extern const char list_under;
    char list_error;

    typedef base_type list_base_type;
    typedef struct Element{
        list_base_type data;
        struct Element* next;
    }element;
    typedef   struct List {
            element* pos_start;
            element* pos_current;
            unsigned list_lenght;
            unsigned list_size;
    }list;
    element* element_gen(list_base_type data);
    list* list_init(unsigned size);
    void list_put(list *l, list_base_type e);
    list_base_type list_get(list *l);
    list_base_type list_read(list *l);
    int list_full(list *l);
    int list_empty(list *l);
    int list_end(list *l);
    unsigned list_count(list *l);
    void pos_move_to_first(list *l);
    void pos_move_to_last(list *l);
    void list_next(list *l);
    void list_move_to(list *l, unsigned int index);
    void list_done(list *l);
    list* list_sum(list *list_1,list *list_2);
    char task_input(FILE *f_in, base_type *t);
    void task_out(base_type t);
#endif
