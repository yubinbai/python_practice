template <typename T> class StackWithMin
{
public:
    StackWithMin(void) {}
    virtual ~StackWithMin(void) {}

    T &top(void);

    void push(const T &value);
    void pop(void);

    const T &min(void) const;

private:
    std::stack<T>   m_data;     // data stack, to store numbers
    std::stack<T>   m_min;      // auxiliary stack, to store minimum numbers
};


template <typename T> void StackWithMin<T>::push(const T &value)
{
    // push the new number into data stack
    m_data.push(value);

    // push the new number into auxiliary stack
    // if it is less than the previous minimum number,
    // otherwise push a replication of the minimum number
    if (m_min.size() == 0 || value < m_min.top())
        m_min.push(value);
    else
        m_min.push(m_min.top());
}

template <typename T> void StackWithMin<T>::pop()
{
    assert(m_data.size() > 0 && m_min.size() > 0);

    m_data.pop();
    m_min.pop();
}

template <typename T> const T &StackWithMin<T>::min() const
{
    assert(m_data.size() > 0 && m_min.size() > 0);

    return m_min.top();
}

template <typename T> T &StackWithMin<T>::top()
{
    return m_data.top();
}
