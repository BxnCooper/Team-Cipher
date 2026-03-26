// Mock data for development - used when backend is unavailable

export const mockUsers = [
  { id: 1, username: 'admin', email: 'admin@university.edu', role: 'admin', created_at: '2026-01-10' },
  { id: 2, username: 'jsmith', email: 'john.smith@university.edu', role: 'user', created_at: '2026-01-15' },
  { id: 3, username: 'emilyr', email: 'emily.r@university.edu', role: 'user', created_at: '2026-02-01' },
  { id: 4, username: 'carlos99', email: 'carlos.m@university.edu', role: 'user', created_at: '2026-02-10' },
  { id: 5, username: 'priya_k', email: 'priya.k@university.edu', role: 'user', created_at: '2026-03-01' },
];

// Using picsum.photos - reliable placeholder image service, no API key needed
// Each ID is a specific photo that always loads
export const mockListings = [
  {
    id: 1,
    title: 'Calculus Textbook (Stewart 9th Ed)',
    description: 'Barely used, no highlights or writing. Covers Calc I and II. Retail is $180, selling for cheap since I graduated.',
    price: 45,
    category: 'textbooks',
    seller_id: 2,
    seller_name: 'jsmith',
    image_url: 'https://picsum.photos/id/24/400/300',
    created_at: '2026-03-20',
  },
  {
    id: 2,
    title: 'MacBook Air M2 - Great Condition',
    description: '2023 MacBook Air M2, 8GB RAM, 256GB SSD. Space Gray. Comes with charger. Minor scuff on bottom, screen is perfect. Battery health 94%.',
    price: 750,
    category: 'electronics',
    seller_id: 3,
    seller_name: 'emilyr',
    image_url: 'https://picsum.photos/id/0/400/300',
    created_at: '2026-03-19',
  },
  {
    id: 3,
    title: 'IKEA Desk + Chair Combo',
    description: 'MALM desk (white, 55") and MARKUS office chair. Both in good shape, just some normal wear. Pick up only - I\'m in the south dorms.',
    price: 120,
    category: 'furniture',
    seller_id: 4,
    seller_name: 'carlos99',
    image_url: 'https://picsum.photos/id/36/400/300',
    created_at: '2026-03-18',
  },
  {
    id: 4,
    title: 'TI-84 Plus CE Graphing Calculator',
    description: 'Works perfectly, color screen. Includes USB cable. Great for any math or engineering class.',
    price: 60,
    category: 'electronics',
    seller_id: 2,
    seller_name: 'jsmith',
    image_url: 'https://picsum.photos/id/60/400/300',
    created_at: '2026-03-17',
  },
  {
    id: 5,
    title: 'North Face Jacket - Men\'s Medium',
    description: 'Black Thermoball jacket, men\'s medium. Worn one season, still in great shape. Super warm and lightweight.',
    price: 85,
    category: 'clothing',
    seller_id: 5,
    seller_name: 'priya_k',
    image_url: 'https://picsum.photos/id/119/400/300',
    created_at: '2026-03-16',
  },
  {
    id: 6,
    title: 'Organic Chemistry (Bruice 8th)',
    description: 'Has some highlighting in chapters 1-6 but otherwise clean. Comes with the study guide. Need gone ASAP.',
    price: 35,
    category: 'textbooks',
    seller_id: 3,
    seller_name: 'emilyr',
    image_url: 'https://picsum.photos/id/42/400/300',
    created_at: '2026-03-15',
  },
  {
    id: 7,
    title: 'Yoga Mat + Resistance Bands Set',
    description: 'Purple yoga mat (thick, non-slip) and a set of 5 resistance bands with handles. Used a few times.',
    price: 25,
    category: 'sports',
    seller_id: 5,
    seller_name: 'priya_k',
    image_url: 'https://picsum.photos/id/26/400/300',
    created_at: '2026-03-14',
  },
  {
    id: 8,
    title: 'Dorm Mini Fridge',
    description: 'Compact 3.2 cu ft mini fridge with small freezer compartment. Works great, selling because I\'m moving off campus.',
    price: 55,
    category: 'furniture',
    seller_id: 4,
    seller_name: 'carlos99',
    image_url: 'https://picsum.photos/id/225/400/300',
    created_at: '2026-03-13',
  },
  {
    id: 9,
    title: 'Sony WH-1000XM4 Headphones',
    description: 'Noise cancelling headphones in black. Incredible sound quality. Comes with case and all cables. Upgrading to XM5.',
    price: 140,
    category: 'electronics',
    seller_id: 2,
    seller_name: 'jsmith',
    image_url: 'https://picsum.photos/id/39/400/300',
    created_at: '2026-03-12',
  },
  {
    id: 10,
    title: 'Wilson Basketball - Indoor/Outdoor',
    description: 'Official size, good grip. Used for intramurals last semester.',
    price: 15,
    category: 'sports',
    seller_id: 4,
    seller_name: 'carlos99',
    image_url: 'https://picsum.photos/id/106/400/300',
    created_at: '2026-03-11',
  },
  {
    id: 11,
    title: 'Intro to Psychology (Myers 13th)',
    description: 'Clean copy, no marks. Required for PSY 101.',
    price: 30,
    category: 'textbooks',
    seller_id: 5,
    seller_name: 'priya_k',
    image_url: 'https://picsum.photos/id/46/400/300',
    created_at: '2026-03-10',
  },
  {
    id: 12,
    title: 'USB-C Hub + Monitor Stand Bundle',
    description: '7-in-1 USB-C hub (HDMI, USB 3.0 x3, SD, microSD, PD) and a wooden monitor riser. Clean desk setup.',
    price: 40,
    category: 'electronics',
    seller_id: 3,
    seller_name: 'emilyr',
    image_url: 'https://picsum.photos/id/180/400/300',
    created_at: '2026-03-09',
  },
];

// Helper to simulate API responses
export function getMockListings({ category, limit, query } = {}) {
  let results = [...mockListings];

  if (category) {
    results = results.filter(l => l.category === category);
  }

  if (query) {
    const q = query.toLowerCase();
    results = results.filter(l =>
      l.title.toLowerCase().includes(q) ||
      l.description.toLowerCase().includes(q) ||
      l.category.toLowerCase().includes(q)
    );
  }

  if (limit) {
    results = results.slice(0, limit);
  }

  return results;
}

export function getMockListing(id) {
  return mockListings.find(l => l.id === Number(id)) || null;
}

export function getMockUser(id) {
  return mockUsers.find(u => u.id === Number(id)) || null;
}

export function getMockUserListings(userId) {
  return mockListings.filter(l => l.seller_id === Number(userId));
}
