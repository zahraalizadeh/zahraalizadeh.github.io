using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace cooking
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void taem_foodBindingNavigatorSaveItem_Click(object sender, EventArgs e)
        {
            this.Validate();
            this.taem_foodBindingSource.EndEdit();
            this.tableAdapterManager.UpdateAll(this.food);

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'food.Taem_food' table. You can move, or remove it, as needed.
            this.taem_foodTableAdapter.Fill(this.food.Taem_food);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Validate();
            this.taem_foodBindingSource.EndEdit();
            this.tableAdapterManager.UpdateAll(this.food);
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            taem_foodBindingSource.AddNew();
            taem_foodBindingSource.MoveLast();
        }

        private void bindingNavigatorAddNewItem_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            taem_foodBindingSource.RemoveCurrent();
            button1_Click(sender, e);


        }
    }
}
